from django.contrib import admin

# own models here.
from .models import Product

admin.site.register(Product)