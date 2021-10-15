from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
]
# The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name.