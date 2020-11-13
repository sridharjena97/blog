from django.contrib import admin
from .models import post,category,author,BlogComment

# Register your models here.
admin.site.register((category,author,BlogComment))

@admin.register(post)
class postAdmin(admin.ModelAdmin):
    class Media:
        js=('js/tinyEditor.js',)
