from django.urls import path
from .views import calculator
from .views import index

urlpatterns = [
        path('index/', index),
        path('<str:met>/<int:v1>/<int:v2>/', calculator),
        
]
