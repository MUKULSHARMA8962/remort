
#import serializers from rest_framework
from rest_framework import serializers
from .models import Product

class ProdectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = '__all__'
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
