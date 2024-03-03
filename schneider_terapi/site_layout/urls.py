from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('eft/', views.eft, name='eft'), # Mads: This is the view function for the EFT page
    path('om_mig/', views.om_mig, name='om_mig'), # Mads: This is the view function for the om_mig page
    path('priser_og_booking/', views.priser_og_booking, name="priser_og_booking"),
    path('terapi/', views.terapi, name='terapi'),
]