from django.urls import path
from app2.views import *

app_name='app2'

urlpatterns=[
    path('app2_fly2/',app2_fly2,name='app2_fly2'),
]