from django.shortcuts import render
from .models import ProductUpdate  # is the model class defined in models.py
# Create your views here.


# SKU: 1112256
# Description: Nike shoes
# Sales Price: 99.99
# Purchase Price: 44.99
SKU = 1112256
Description = 'Nike shoes'
Sales_Price = 99.99
Purchase_Price = 44.99


def my_view(request, *args, **kwargs):
    # Insert in the database
    ProductUpdate.objects.create(ProductSKU=SKU, ProductDescription=Description, ProductSellingPrice=Sales_Price, ProductPurchasePrice=Purchase_Price)

    # Getting all the stuff from database
    query_results = ProductUpdate.objects.all();

    # Creating a dictionary to pass as an argument
    context = {'query_results': query_results}

    # Returning the rendered html
    return render(request, "home.html", context)