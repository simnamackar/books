from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render,redirect
from .forms import Authorform,Bookform
# Create your views here.
from .models import bk

def listview(request):
    books=bk.objects.all()
    paginator=Paginator(books,4)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)

    except EmptyPage:
        page=paginator.page(page_number.num_pages)
    return render(request,'viewbook.html',{'books':books,'page':page})

def detailsview(request,book_id):
    book=bk.objects.get(id=book_id)
    return render(request,'detailsview.html',{'book':book})

def updateview(request,book_id):

    book=bk.objects.get(id=book_id)
    if request.method=='POST':
        form = Bookform(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect('booklist')
    else:
        form=Bookform(instance=book)
    return render(request,'updateview.html',{'form':form})
def deleteview(request,book_id):
    book=bk.objects.get(id=book_id)
    if request.method=="POST":
        book.delete()
        return redirect('booklist')
    return render(request,'deleteview.html',{'book':book})

def createbook(request):
    books=bk.objects.all()
    if request.method=='POST':
        form=Bookform(request.POST,request.FILES)
        # print(form)

        if form.is_valid():
            form.save()
            return redirect('list_view')

    else:
        form=Bookform()
    return render(request,'book.html',{'form':form,'books':books})

def createauthor(request):
    if request.method=='POST':
        form=Authorform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createbook')
    else:
        form=Authorform()
    return render(request,'author.html',{'form':form})


def index(request):
    return render(request,'base.html')

def searchbook(request):
    Query=None
    books=None
    if 'Q' in request.GET:
        Query=request.GET.get('Q')
        books=bk.objects.filter(Q(title__icontains=Query))

    else:
        books=[]

    context={'books':books,'Query':Query}

    return render(request,'search.html',context)

def searchauthor(request):
    Query=None
    author=None
    if 'Q' in request.GET:
        Query=request.GET.get('Q')
        author=bk.objects.filter(Q(name__icontains=Query))

    else:
        author=[]

    context={'author':author,'Query':Query}

    return render(request,'searchauthor.html',context)




 # book=bk.objects.get(id=book_id)
    # if request.method == 'POST':
    #     title = request.POST.get('title')
    #     price = request.POST.get('price')
    #     book.title=title
    #     book.price=price
    #     book.save()
    #     return redirect('/')
    # return render(request, 'updateview.html', {'book': book})

# def createbook(request):
#     books = bk.objects.all()
#     if request.method=='POST':
#         title=request.POST.get('title')
#         price=request.POST.get('price')
#
#         book=bk(title=title,price=price)
#         book.save()
#     return render(request,'book.html',{'books':books})
