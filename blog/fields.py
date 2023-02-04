from django import forms
from django.db import models
from django.core.exceptions import ValidationError

#define model field:
class myTimestampField(models.IntegerField):
    def __init__(self, *args, **kwargs):
       # kwargs['max_length'] = 104
       super().__init__(*args, **kwargs)
    
    def formfield(self, **kwargs):
        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        defaults = {
            'form_class': myTimestampFormField,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)
    
    # def to_python(self, value):
    #     print("---");
    #     return 1673568000000;
    
    # def validate(self, value):
    #     print("-+-");
    #     super().validate(value);
    #     return;
                 
class myTimestampFormField(forms.DateField):
    widget=forms.widgets.DateInput(attrs={'type': 'date'})
    # def clean(self, value):
    #     try:
    #         return value.upper()
    #     except:
    #         raise ValidationError
            
    # def to_python(self, value):
    #     print("---");
    #     return 1673568;