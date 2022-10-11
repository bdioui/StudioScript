from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Main'
urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('graphisme', views.graphisme, name="graphisme"),
]
