from django.contrib import admin

# Register your models here.
from .models import bk,Author
admin.site.register(bk)
admin.site.register(Author)