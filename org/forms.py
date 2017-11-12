from django import forms

class RegForm(forms.Form):
    your_name = forms.CharField(label='Your Name',max_length=100)
    your_email = forms.EmailField(label='Your Email')
    for_no = forms.IntegerField(label='Your Contact')
    date = forms.DateField(label='Date')
    doctor = forms.CharField(label='Doctor')
