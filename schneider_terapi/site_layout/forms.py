from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
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
        widget=forms.Textarea,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "contact_form"
        self.helper.form_class = "blueForms"
        self.helper.form_method = "post"
        self.helper.form_action = "index" # Submits to 'index' view !SET IN JS!

        self.helper.add_input(Submit('submit', 'Indsend'))

        self.helper.layout = Layout(
            FloatingField("name"),
            Row(
                Column(FloatingField("email")),
                Column(FloatingField("phone_number")),
                css_class="form_row"
            ),
            FloatingField("message")
        )