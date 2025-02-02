
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gettoknow/', views.gettoknow, name='gettoknow'),
    path('us/', views.us, name='us'),
    path('sign/', views.sign, name='sign'),
    path('events/', views.events, name='events'),
    path('feature/', views.feature, name='feature'),
]
