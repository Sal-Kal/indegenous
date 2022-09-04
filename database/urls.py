from django.urls import path
from . import views

urlpatterns = [
    path('asgard/',views.index),
    path('get/<str:key>',views.getDetails)
]