from django.shortcuts import render


from .forms import *


def index(request):
    contact_form = ContactForm()
    return render(request, "site_layout/index.html", {
        "contact_form": contact_form
    })

# Mads: This is the view function for the EFT page + om_mig
def eft(request): 
    return render(request, "site_layout/eft.html")

def om_mig(request):
    return render(request, "site_layout/om_mig.html")
