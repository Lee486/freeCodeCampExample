from django.urls import path

from .views import (dynamicLookupView, productDelete, productDetailView, productCreateView, renderInitialData, productList)

app_name = "products"
urlpatterns = [
    path('detail/', productDetailView),
    path('create/', productCreateView),
    path('render/', renderInitialData),
    path('list/', productList, name = "product-list"),
    path('<int:id>/', dynamicLookupView, name = 'product-detail'),
    path('<int:id>/delete', productDelete, name = 'product-delete'),
    
]
