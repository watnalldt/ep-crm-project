from captcha.fields import ReCaptchaField
from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    contact_email = forms.EmailField(max_length=50, required=True)
    company = forms.CharField(max_length=50, required=False)

    message = forms.CharField(
        required=True, widget=forms.Textarea, label="Your Message Here:"
    )
    captcha = ReCaptchaField()
