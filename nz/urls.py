from nz.views import *
from django.urls import path
app_name='southee'
urlpatterns=[
    path('williamson/',williamson,name='williamson'),
    path('ravindra/',ravindra,name='ravindra'),
]