from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return httpResponse('home')
def products(request):
    return httpResponse('products')
def customer(request):
    return httpResponse('customer')