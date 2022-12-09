from myappstaff.models import *
from django.forms import ModelForm


class All_CategoryTypeForm(ModelForm):
    class Meta:
        model = CategoryType
        fields = ['name_CategoryType']

class All_CategoryStatusForm(ModelForm):
    class Meta:
        model = CategoryStatus
        fields = ['name_CategoryStatus']     