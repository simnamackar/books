
from django.urls import path
from . import views
urlpatterns = [


 path('viewlist/',views.listview,name='booklist'),
 path('userdetailsview/<int:book_id>/',views.detailsview,name='details'),
 path('usersearch/',views.usersearch,name='usersearch'),
 path('addtocart/<int:book_id>/',views.add_to_cart,name='addtocart'),
 path('viewcart/',views.view_cart,name='viewcart'),
 path('increasequantity/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
 path('decreasequantity/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
 path('removecart/<int:item_id>/',views.remove_cart,name='remove_cart'),
 path('create-checkout-session/',views.create_checkout_session,name='create-checkout-session'),
 path('success/',views.success,name='success'),
 path('cancel/',views.cancel,name='cancel')
 ]

