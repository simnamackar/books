from django.contrib import admin
from .models import UserProfile,logintable
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(logintable)