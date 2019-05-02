from django.shortcuts import render, get_object_or_404
from .models import TechType, Product, Review

# Create your views here.
def index(request):
    return render(request, 'TechReviewApp/index.html')

def getTypes(request):
    types_list=TechType.objects.all()
    return render(request, 'TechReviewApp/types.html',{'types_list' : types_list})

def getProducts(request):
    products_list=Product.objects.all()
    return render(request, 'TechReviewApp/products.html',{'products_list': products_list})

def productDetails(request, id):
    prod=get_object_or_404(Product, pk=id)
    reviewcount=Review.objects.filter(product=id).count()
    reviews=Review.objects.filter(product=id)
    context={
        'prod' : prod,
        'reviewcount' : reviewcount,
        'reviews' : reviews,
    }
    return render(request, 'TechReviewApp/proddetails.html', context=context)

