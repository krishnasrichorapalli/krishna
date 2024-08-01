from django.contrib import admin
from django.contrib.admin.decorators import register
# Register your models here.
from .models import Category
@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display=['category_name','slug','description','cat_image']