# webscraping/forms.py
from django import forms

class WebsiteForm(forms.Form):
    website_url = forms.URLField(label='Website URL')
