from django import forms
from django.forms import ModelForm
from .models import Product


class CompForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('owner', 'title', 'description', 'delivery', 'collection', 'min_ticket', 'max_ticket', 'alternative_prize', 'end_date', 'charity', 'char_percent', 'image',
                  )
        labels = {
            'owner': '',
            'title': '',
            'description': '',
            'delivery': '',
            'collection': '',
            'min_ticket':  '',
            'max_ticket': '',
            'quantity_winners': '',
            'alternative_prize': '',
            'end_date': '',
            'charity': '',
            'char_percent': '',
            'image': '',
        }
        widgets = {
            'owner': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Owner'}),
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Description'}),
            'delivery': forms.Select(attrs={'class':'form-select', 'placeholder':'Delivery Options'}),
            'collection': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Collection'}),
            'min_ticket':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'Minimum Tickets'}),
            'max_ticket': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Maximum Tickets'}),
            'quantity_winners': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Number of Winners'}),
            'alternative_prize': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Alternative Prize'}),
            'end_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'End Date'}),
            'charity': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of Charity'}),
            'char_percent': forms.Select(attrs={'class':'form-select', 'placeholder':'Percentage to Charity'}),
            # 'image': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Image'}),
        }
        
        
        
