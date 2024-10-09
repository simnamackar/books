from django.db import models
from django.db import models
from book_app.models import bk
from loginapp.models import UserProfile
from django.contrib.auth.models import User





# Create your models here.
class Cart(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(bk)
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    book = models.ForeignKey(bk, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)