import json
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from smtplib import SMTPException

from .forms import *

TO_EMAIL = 'kontakt@schneiderterapi.dk'

def index(request):

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            
            name = contact_form.cleaned_data['name']
            message = contact_form.cleaned_data['message']
            phone_number = contact_form.cleaned_data['phone_number']
            email = contact_form.cleaned_data['email']

            html = render_to_string('site_layout/contactform.html', {
                'name': name,
                'message': message,
                'email': email,
                'phone_number': phone_number
            })

            try:
                send_mail(contact_form.cleaned_data['name'],
                      contact_form.cleaned_data['message'],
                      TO_EMAIL, # TO_EMAIL is the same for sender as well as recipient
                      [TO_EMAIL],
                      html_message=html,
                      fail_silently=False)
            except SMTPException as e:
                print(f'There was an error, {e}') 
            except:
                print('There was an error sending this mail.')

        return redirect('index')

    contact_form = ContactForm()
    return render(request, "site_layout/index.html", {
        "contact_form": contact_form
    })


# Mads: This is the view function for the EFT page + om_mig
def eft(request): 
    return render(request, "site_layout/eft.html")

def om_mig(request):
    return render(request, "site_layout/om_mig.html")

def priser_og_booking(request):
    return render(request, "site_layout/priser_og_booking.html")

def terapi(request):
    return render(request, "site_layout/terapi.html")
