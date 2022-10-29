from django.urls import path 
from . import views

app_name = 'product'

urlpatterns=[ 
    path('',views.product,name='product'),
    path('add/',views.add_item,name='add_product'),
    path('<str:slug>/',views.product_detail,name='product_detail'),

]