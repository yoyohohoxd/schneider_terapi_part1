from django.shortcuts import render


from .forms import *


def index(request):
    contact_form = ContactForm()
    return render(request, "site_layout/index.html", {
        "contact_form": contact_form
    })