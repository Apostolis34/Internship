from django.contrib import admin

from .models import mvContactPerson, mvSupplierClient, mvProductCategory, mvProduct, ProductUpdate
# Register your models here.
admin.site.register(mvContactPerson)
admin.site.register(mvSupplierClient)
admin.site.register(mvProductCategory)
admin.site.register(mvProduct)
admin.site.register(ProductUpdate)