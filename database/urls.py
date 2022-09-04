from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('get/<str:key>',views.getDetails),
    path('populate/',views.populate)
]