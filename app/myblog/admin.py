from django.contrib import admin
from .models import post,category,author,BlogComment

# Register your models here.
admin.site.register((post,category,author,BlogComment))
