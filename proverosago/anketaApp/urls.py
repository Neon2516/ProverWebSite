from django.urls import path
from . import views



urlpatterns = [
    path('', views.anketa, name='anketa'),
    path('results/', views.results, name='results'),
    path('get-models/', views.get_models, name='get_models')
]