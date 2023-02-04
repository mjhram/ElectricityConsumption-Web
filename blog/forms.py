from django import forms
from datetime import datetime 
import datetime as dt
from .models import ElecUnits
from django.utils import timezone

# class NameForm(forms.ModelForm):
#     #your_name = forms.CharField(label='Your name', max_length=100)
#     YN=[
#         (1, 'Yes'),
#         (0, 'No')
#     ]
#     #no = forms.AutoField(db_column='No', primary_key=True)  # Field name made lowercase.
#     time = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))  # This field type is a guess.
#     # prevdateinmillisec = forms.IntegerField()  # Field name made lowercase.
#     nextdateinmillisec = forms.IntegerField(initial=1671408000000)  # Field name made lowercase.
#     # prevreading = forms.IntegerField()  # Field name made lowercase.
#     # nextreading = forms.IntegerField()  # Field name made lowercase.
#     # price = forms.CharField(max_length=15)
#     # calcstr = forms.CharField( max_length=100)  # Field name made lowercase.
#     #isitbill = forms.ChoiceField(choices=YN)  # Field name made lowercase.
#     class Meta:
#         model = ElecUnits
#         fields = ['nextdateinmillisec']
           
    
class FormNew(forms.ModelForm):
        # self.price.widget.attrs['readonly'] = True
    
    YN=[
             (True, 'Yes'),
             (False, 'No')
         ]
    elecUnitObj=None
    isSave = forms.BooleanField(initial=False, label='Save to DB', required=False)  # This field type is a guess.
    # time = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))  # This field type is a guess.


    def __init__(self, *args, **kwargs):
        super(FormNew, self).__init__(*args, **kwargs)
        if FormNew.elecUnitObj is not None:
        #     print("else")
        # else:
            self.fields['prevdateinmillisec'].initial = datetime.fromtimestamp(FormNew.elecUnitObj.prevdateinmillisec/1000) #1673568000.000) # dt.date.today()#'01-02-2023'#datetime.date.today()#FormNew.elecUnitObj.nextdateinmillisec
            self.fields['nextdateinmillisec'].initial = datetime.fromtimestamp(FormNew.elecUnitObj.nextdateinmillisec/1000) #1673568000.000) # dt.date.today()#'01-02-2023'#datetime.date.today()#FormNew.elecUnitObj.nextdateinmillisec
            self.fields['prevreading'].initial = FormNew.elecUnitObj.prevreading
            self.fields['nextreading'].initial = FormNew.elecUnitObj.nextreading
            self.fields['isitbill'].initial = FormNew.elecUnitObj.isitbill
            FormNew.elecUnitObj = None
    
        
    class Meta:
        model = ElecUnits
        fields = [ 'prevdateinmillisec', 'prevreading'
                  , 'nextdateinmillisec', 'nextreading', 'isitbill', 
                  'price', 'calcstr']
        labels = {
            'prevdateinmillisec': 'Prev Date',
            'prevreading': 'Prev Reading',
            'nextdateinmillisec': 'Next Date',
            'nextreading': 'Next Reading',
            'isitbill': 'Is It Bill',
            'price': 'Price',
            'calcstr': 'Calc String',
            
        }
        
        widgets = {
        #       'nextdateinmillisec': forms.widgets.DateInput(attrs={'type': 'date'})
            'price': forms.HiddenInput(),
            'calcstr': forms.HiddenInput(),
            # 'isitbill': forms.Select(attrs={
            #     'class': 'form-control',
            #  }),
            # 'prevdateinmillisec': forms.widgets.DateInput(attrs={'type': 'date'})
        }
    
    # prevdateinmillisec = forms.DateField(initial = datetime.today(), widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    # prevreading = forms.IntegerField(initial=19)
    # nextdateinmillisec = forms.DateField(initial = datetime.today(), widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    # nextreading = forms.IntegerField(initial=119)

    # def print_hello_world(self):
    #      print('Hello World')
    
    # def clean_nextdateinmillisec(self):
    #     data = self.cleaned_data['nextdateinmillisec']
    #     print("---")
    #     print(data)
    #     # do some stuff
    #     data=datetime.fromisoformat(data.isoformat())
    #     data = data.timestamp()
    #     print(data)
    #     print("--")
        
    #     return data
    
    def clean_prevdateinmillisec(self):
        data = self.cleaned_data['prevdateinmillisec']
        #print("+++")
        # print(data)
        # do some stuff
        data=datetime.fromisoformat(data.isoformat())
        data = data.timestamp()*1000
        # print(data)
        return data
    
    def clean_nextdateinmillisec(self):
        data = self.cleaned_data['nextdateinmillisec']
        #print("++++")
        # print(data)
        # do some stuff
        data=datetime.fromisoformat(data.isoformat())
        data = data.timestamp()*1000
        # print(data)
        return data

    