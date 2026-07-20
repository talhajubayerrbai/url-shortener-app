from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stats/<str:code>/', views.stats, name='stats'),
    path('<str:code>', views.redirect_short, name='redirect_short'),
]
