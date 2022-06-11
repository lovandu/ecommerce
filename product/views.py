from django.shortcuts import render
from django.views import View
from .models import *
from django.http import *

# Create your views here.
class GetProduct(View): 
    def get(self, request):
        product=Product.objects.all()
        return render(request, 'product/index.html',{'product':product})