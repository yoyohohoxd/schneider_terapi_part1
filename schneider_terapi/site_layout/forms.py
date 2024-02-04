from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_bootstrap5.bootstrap5 import FloatingField
from django import forms

class ContactForm(forms.Form):

    name = forms.CharField(
        label = "Navn",
        max_length = 100,
        required = True,
    )

    email = forms.CharField(
        label = "Email",
        max_length = 80,
        required = True,
    )

    phone_number = forms.IntegerField(
        label = "Telefon",
        required = True,
    )

    message = forms.CharField(
        label = "Besked",
        required = True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "contact_form"
        self.helper.form_class = "blueForms"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_survey"

        self.helper.add_input(Submit('submit', 'Indsend'))
        self.helper.layout = Layout(
            FloatingField("name", "email", "phone_number", "message")
        )