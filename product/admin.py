from django.contrib import admin
from product.models import Category, Product,Images

# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','parent','status']
    list_filter=['status']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status','image_tag']
    list_filter = ['category']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images)
