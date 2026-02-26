from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('save-fatigue/', views.save_fatigue, name='save_fatigue'),
]