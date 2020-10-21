from django.contrib import admin
from .models import post,category,author

# Register your models here.
admin.site.register(post),
admin.site.register(category),
admin.site.register(author)
