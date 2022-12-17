from myapp.models import *
from django.forms import ModelForm

class ListRecForm(ModelForm):
    class Meta:
        model = ListFromRec
        fields = ['name', 'brand', 'quantity','price', "link", 'description']
        
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_user']