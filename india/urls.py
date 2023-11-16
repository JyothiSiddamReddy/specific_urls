from india.views import *
from django.urls import path
app_name='gill'

urlpatterns=[
    path('virat/',virat,name='virat'),
    path('shreyas/',shreyas,name='shreyas'),
]