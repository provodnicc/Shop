from .models import Category
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

admin.site.register(Category, MPTTModelAdmin)
