from django.shortcuts import render
from .serializer import PostSerializer,CategorySerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from .models import Post,Category
from rest_framework.viewsets import ModelViewSet

# Create your views here.

#concrete api view yazdık burada
class CategoryListCV(ListCreateAPIView):
	queryset= Category.objects.all()
	serializer_class = CategorySerializer
	filterset_fields=['name']
	search_fields=['^name']
	ordering_fields=['id']

class CategoryDetailCV(RetrieveUpdateDestroyAPIView):
	queryset= Category.objects.all()
	serializer_class = CategorySerializer

#!modelviewset
class PostMVS(ModelViewSet):
	filterset_fields=['title','category']
	search_fields=['^title']
	ordering_fields=['id']
	queryset=Post.objects.all()
	serializer_class=PostSerializer
