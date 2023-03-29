from django.shortcuts import render
from rest_framework.views import APIView
from.models import *
from rest_framework.response import Response
from rest_framework import status
from.serializers import ProdectSerializer
# Create your views here.
import requests
from django.http import JsonResponse
class Productview(APIView):
    def get(self,request):
        Products=Product.objects.all()
        serializer=ProdectSerializer(Products,many=True)
        return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)

    
def get_data_from_api(request):
    # Make a GET request to the API URL
    api_url = "http://127.0.0.1:8000/product"
    response = requests.get(api_url)

    # Get the response data
    data = response.json()

    # Create a JSON response with the data
    response_data = {"status": "success", "data": data}
    return JsonResponse(response_data)

from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view(['POST'])
# def process_data(request):
#     data = request.data
#     # process data here
#     response = {'status': 'success', 'message': 'Data processed successfully.'}
#     return Response(response)

# @api_view(['GET'])
# def process_data(request):
#     id = request.query_params.get('id', None)
#     if id is not None:
#         # process id here
#         response = {'status': 'success', 'message': f'Processed ID: {id}'}
#     else:
#         response = {'status': 'error', 'message': 'Missing ID parameter.'}
#     return Response(response)

from rest_framework.decorators import api_view
from rest_framework.response import Response


from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def process_data(request):
    data = request.data
    key1 = data.get('key1', None)
    key2 = data.get('key2', None)
    if key1 is not None and key2 is not None:
        # process key1 and key2 here
        response = {'status': 'success', 'message': 'Data processed successfully.'}
        print(f"key1: {key1}, key2: {key2}")
    else:
        response = {'status': 'error', 'message': 'Missing key1 or key2 parameter.'}
    return Response(response)
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def index(request):
    return render(request, 'index.html',)
