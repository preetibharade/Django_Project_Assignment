# forms.py
from django import forms
from django.forms import widgets
from django.urls import reverse_lazy
from .models import Candidatedirectory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from datetime import datetime

class CandidateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('create_candidate')
        self.helper.add_input(Submit('submit', 'Submit'))
    
    
    class Meta:
        model = Candidatedirectory
        fields = '__all__'
        widgets = {
            'first_name' : forms.TextInput(attrs ={'type' : 'text', 'required':True}),
            'last_name' : forms.TextInput(attrs ={'type' : 'text', 'required':True}),
            'created_date' : forms.DateInput(attrs ={'type' : 'date', 'required':True, 'max' : datetime.now().date()}),
            'email' : forms.EmailInput(attrs = {'type': 'email', 'required':True} ),
            'dob' : forms.DateInput(attrs ={'type' : 'date', 'required':True, 'max' : datetime.now().date()}),
            'contact_np_primary' : forms.NumberInput(attrs = {'size':'10','maxlength':'10', 'class':'phone','required':True}),
            'pincode' : forms.NumberInput(attrs = {'size':'6','maxlength':'6', 'class':'phone','required':True}),
            'modified_date' : forms.DateInput(attrs ={'type' : 'date', 'required':True,'max' : datetime.now().date()}),
        }