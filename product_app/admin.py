from django.contrib import admin

from .models import SpProduct,SpDivision,SpSubCategory,SpCategory

admin.site.register(SpProduct)
admin.site.register(SpCategory)
admin.site.register(SpDivision)
admin.site.register(SpSubCategory)
