
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('community/', views.community, name='community'),
    path('gettoknow/', views.gettoknow, name='gettoknow'),
    path('us/', views.us, name='us'),
    path('sign/', views.sign, name='sign'),
    path('events/', views.events, name='events'),
]
