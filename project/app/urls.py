from django.contrib import admin
from django.contrib.admin import sites
from django.urls import path
from . import views

from django.urls import path
from .views import BookList, BookDetail
# from tracker1.models import ITPortal
from.views import Productview,get_data_from_api,process_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index),
    path('product',Productview.as_view()),
    #path('api/myobjects/<int:pk>/', views.MyObjectDetailView.as_view()),
    path('api/data/', get_data_from_api, name='get_data_from_api'),
    path('process_data/', process_data),
    path('books/', BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
  
  
]