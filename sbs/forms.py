#-*- coding: utf-8 -*-
from django import forms
from .models import Items
from datetime import datetime

class m1(forms.ModelForm):
   class Meta:
     model= Items
     CHOICES = (('PENDING', 'PENDING'),('BOUGHT', 'BOUGHT'),('NOT AVAILABLE', 'NOT AVAILABLE'),) 
     fields=['Item','Quantity','status','date',]
     widgets={
            'Item':forms.TextInput(attrs={'placeholder':'enter your channel name'}),
            'Quantity':forms.TextInput(),
            'status':forms.TextInput(),
            'date':forms.DateInput(attrs={'class':'border rounded w-full py-2 px-4 outline-none focus:shadow-outline'})
        }

class m(forms.Form): 
    CHOICES = (('PENDING', 'PENDING'),('BOUGHT', 'BOUGHT'),('NOT AVAILABLE', 'NOT AVAILABLE'),) 
    Item = forms.CharField(max_length=50)  
    Quantity  = forms.CharField(max_length = 100) 
    status = forms.ChoiceField(choices=CHOICES)
    date = forms.DateField(initial=datetime.today)

