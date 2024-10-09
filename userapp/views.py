from django.conf import settings
from django.contrib import messages
# from .forms import Authorform,Bookform
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render,redirect
from django.urls import reverse

from .models import Cart,CartItem
from book_app.models import bk
import stripe
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect
# from django.urls import reverse

def add_to_cart(request, book_id):
    book = bk.objects.get(id=book_id)
    try:
            if request.user.is_authenticated:

                if book.quantity > 0:
                    cart, created = Cart.objects.get_or_create(user=request.user)
                    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, book=book)

                    if not item_created:
                        cart_item.quantity += 1
                        cart_item.save()

            return redirect('viewcart')

    except:
            messages.error("please login")

def view_cart(request):

        cart, cart_created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.cartitem_set.all()
        cart_item = CartItem.objects.all()
        total_price = sum(item.book.price * item.quantity for item in cart_items)
        total_items = cart_items.count()

        context = {
            'cart_items': cart_items,
            'cart_item': cart_item,
            'total_price': total_price,
            'total_items': total_items
        }
        return render(request, 'cart.html', context)



def listview(request):
    books=bk.objects.all()
    paginator=Paginator(books,4)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)

    except EmptyPage:
        page=paginator.page(page_number.num_pages)
    return render(request,'userviewbook.html',{'books':books,'page':page})

def detailsview(request,book_id):
    book=bk.objects.get(id=book_id)
    return render(request,'userdetailview.html',{'book':book})

# Create your views here.

def usersearch(request):
    Query=None
    books=None
    if 'Q' in request.GET:
        Query=request.GET.get('Q')
        books=bk.objects.filter(Q(title__icontains=Query) | Q(author__name__icontains=Query))

    else:
        books=[]

    context={'books':books,'Query':Query}

    return render(request,'usersearch.html',context)

def increase_quantity(request,item_id):
    cart_item=CartItem.objects.get(id=item_id)
    if cart_item.quantity < cart_item.book.quantity:
        cart_item.quantity+=1
        cart_item.save()
    return redirect('viewcart')
def decrease_quantity(request,item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('viewcart')

def remove_cart(request,item_id):
    try:
        cart_item=CartItem.objects.get(id=item_id)
        cart_item.delete()
    except cart_item.DoesNotExist:
        pass
    return redirect('viewcart')
def create_checkout_session(request):
    cart_items=CartItem.objects.all()

    if cart_items:
        stripe.api_key=settings.STRIPE_SECRET_KEY
        if request.method=='POST':
            line_items=[]
            for cartitem in cart_items:
                if cartitem.book:
                    line_item={
                        'price_data':{
                            'currency':'INR',
                            'unit_amount': int(cartitem.book.price* 100),
                            'product_data':{
                                'name':cartitem.book.title
                            },
                        },
                        'quantity':cartitem.quantity

                    }
                    line_items.append(line_item)

                if line_items:
                    checkout_session=stripe.checkout.Session.create(
                        payment_method_types=['card'],
                        line_items=line_items,
                        mode='payment',
                        success_url=request.build_absolute_uri(reverse('success')),
                        cancel_url=request.build_absolute_uri(reverse('cancel'))
                    )
                    return redirect(checkout_session.url,code=303)

def success(request):
    cart_items=CartItem.objects.all()
    for cartitem in cart_items:
        product=cartitem.book
        if product.quantity >= cartitem.quantity:
            product.quantity-=cartitem.quantity
            product.save()
    cart_items.delete()
    return render(request,'success.html')

def cancel(request):
    return render(request,'user/cancel.html')

