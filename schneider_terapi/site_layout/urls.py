from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('eft/', views.eft, name='eft'), # Mads: This is the view function for the EFT page
]