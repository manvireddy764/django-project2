from django.urls import path
from app1.views import *

app_name='app1'

urlpatterns=[
    path('app1_fly1/',app1_fly1,name='app1_fly1'),
]