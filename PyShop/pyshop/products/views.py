from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})


def index1(request):
    return HttpResponse('New Products')


def index2(request):
    return HttpResponse('Index 2 Response')


