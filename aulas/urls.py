from django.urls import path
from . import views

app_name='aulas'

urlpatterns = [
    path('', views.cadastro, name='cadastro'),
    path('cadastrook/', views.cadastrook, name='cadastrook'),
]