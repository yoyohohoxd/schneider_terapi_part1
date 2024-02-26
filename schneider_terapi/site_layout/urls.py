from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('eft/', views.eft, name='eft'), # Mads: This is the view function for the EFT page
    path('om_mig/', views.om_mig, name='om_mig'), # Mads: This is the view function for the om_mig page
    path('send_mail/', views.send_mail, name='send_mail')
]