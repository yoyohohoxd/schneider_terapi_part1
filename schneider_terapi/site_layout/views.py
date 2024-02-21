from django.shortcuts import render, redirect
from django.core.mail import send_mail


from .forms import *


def index(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            print('form is valid')
            

            send_mail(contact_form.cleaned_data['name'],
                      contact_form.cleaned_data['message'],
                      contact_form.cleaned_data['email'],
                      ['madse@live.dk'])
            
        return redirect('index')

    else:
        contact_form = ContactForm()
        return render(request, "site_layout/index.html", {
            "contact_form": contact_form
        })

# Mads: This is the view function for the EFT page + om_mig
def eft(request): 
    return render(request, "site_layout/eft.html")

def om_mig(request):
    return render(request, "site_layout/om_mig.html")
