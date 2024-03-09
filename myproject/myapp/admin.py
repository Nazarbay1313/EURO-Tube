from django.contrib import admin

from myapp.models import Comment, Product, Tag

# Register your models here.

admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Comment)
