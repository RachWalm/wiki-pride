
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('comingout/', views.comingout, name='comingout'),
    path('community/', views.community, name='community'),
    path('culture/', views.culture, name='culture'),
    path('history/', views.history, name='history'),
]
