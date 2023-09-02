from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from product.serializers import ProductSerializer

from product.models import Product

class ListProductAPIView(ListAPIView):
    """This endpoint list all of the available Products from the database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class CreateProductAPIView(CreateAPIView):
    """This endpoint allows for creation of a Product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




class DestroyProductAPIView(DestroyAPIView):
    """This endpoint allows for creation of a Product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer





class UpgradeProductAPIView(UpdateAPIView):
    """This endpoint allows for creation of a Product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer





# Create your views here.
def index(request):
    return HttpResponse("Hello World !")