"""Fifa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index),
    path('players/', views.players, name='players'),
    path('positions/', views.allPositions, name='positions'),
    path('getDetails/', views.getDetails, name='details'),
    path('leagues/', views.allLeagues, name='leagues'),
    path('statistics/', views.statistics),
    path('clubs/', views.allClubs),
    path('nationalities/', views.allCountries, name='nationalities'),
    path('delete/', views.deletePlayer),
    path('news/', views.news1),
    path('news1/', views.news),
    path('download/',views.table, name= 'download'),
]
