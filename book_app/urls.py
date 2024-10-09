
from django.urls import path
from . import views
urlpatterns = [

 path("create-book/",views.createbook,name='createbook'),
 path("author/",views.createauthor,name='author'),
 path('list_view/',views.listview,name='list_view'),
 path('detailsview/<int:book_id>/',views.detailsview,name='details'),
 path('updateview/<int:book_id>/',views.updateview,name='update'),
 path('deleteview/<int:book_id>/',views.deleteview,name='delete'),
 path('index/',views.index),
 path('search/',views.searchbook,name='search'),
 # path('searchauthor/',views.searchauthor,name='searchauthor')
 # path('authorupdate/',views.updateauthor,name='authorupdate'),
 # path('authordelete/',views.authordelete,name='authordelete')
]

