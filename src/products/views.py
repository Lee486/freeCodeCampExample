from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm
from .models import Product

#previously:
def productCreateView(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "products/create.html", context)

#part two: about learning get/post
# def productCreateView(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == "POST":
#         newTitle = request.POST.get('title')
#         print(newTitle)
#     context = {}
#     return render(request, "product/create.html", {})

# #version 3: where we talk about how it moves/is cleaned
# def productCreateView(request):
#     myForm = RawProductForm()
#     if request.method == "POST":
#         myForm = RawProductForm(request.POST)
#         if myForm.is_valid():
#             #now data is good 
#             print(myForm.cleaned_data)
#             Product.objects.create(**myForm.cleaned_data)
#         else:
#             print(myForm.errors)

#     context = {
#         "form": myForm
#     }
#     return render(request, "product/create.html", context)

def productDetailView(request):
    obj = Product.objects.get(id = 1)
    # context = {
    #     'title': obj.title,
    #     'description' : obj.description 
    # }
    context = {
        'object': obj
    }
    return render(request, "product/detail.html", {})

def renderInitialData(request):        
    initial_data = {
        'title': "New Title"
        }
    obj = Product.objects.get(id=1)
    form = RawProductForm(request.POST or None, instance = obj)
    context = {
        'form': form
        }
    return render(request, "products/create.html", context)

def dynamicLookupView(request, id):
    obj = get_object_or_404(Product, id=id) #using django's builtin structure -> preferred
    #using http and a try box
    # try: 
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        "object" : obj 
    }
    return render(request, "product/detail.html", context )

def productDelete(request, id):
    obj = get_object_or_404(Product, id=id)
    #obj.delete() #default is get, so make it post
    if request.method == "POST":
        obj.delete()
        return redirect('../')
    
    context = {
        "object" : obj 
    }
    return render(request, "product/delete.html", context )


def productList(request):
    queryset = Product.objects.all() #list of all the objects
    context = {
        "object_list": queryset
    }
    return render(request, "product/list.html", context )