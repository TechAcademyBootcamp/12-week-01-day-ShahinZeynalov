from django import forms
from .models import CustomModel,State


# class CustomForm(forms.Form):
#
#     STATES = (
#         (1,'Choose')
#     )
#     email = forms.EmailField(widget = forms.EmailInput(attrs={
#         'class':"form-control",
#         'id':"inputEmail4",
#         'placeholder':'Email'
#     }))
#     password = forms.CharField(widget = forms.PasswordInput(attrs={
#         'class':'form-control',
#         'placeholder':'Password',
#         'id':'inputPassword4',
#
#     }))
#     address = forms.CharField(label='Address 1',widget = forms.TextInput(attrs={
#         'class':'form-control',
#         'id':'inputAddress',
#         'placeholder':'1234 Main St',
#     }))
#     address1 = forms.CharField(label = 'Address 2',widget=forms.TextInput(attrs={
#         'class':'form-control',
#         'id':'inputAddress2',
#         'placeholder':'Apartment, studio, or floor',
#     }))
#
#     city = forms.CharField(widget=forms.TextInput(attrs={
#         'class':'form-control',
#         'id':'inputCity',
#     }))
#     c =[("1", "Option 1"), ("2", "Option 2")]
#
#     state = forms.ChoiceField(choices=c,widget=forms.Select(attrs={
#         'class':'form-control',
#     }))
#     zip = forms.CharField(widget=forms.TextInput(attrs={
#         'class':'form-control',
#         'id':'inputZip'
#     }))
#     check = forms.BooleanField(label = 'Check me out',initial=False,widget = forms.CheckboxInput(attrs={
#         'class':'form-check-input',
#         'id':'gridCheck',
#
#     }))


class CustomForm(forms.ModelForm):
    email = forms.EmailField(label='Email address',
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'id': 'exampleInputEmail1',
                                 }))

    password = forms.CharField(widget = forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Password',
            'id':'inputPassword4',

        }))

    address1 = forms.CharField(label='Address 1',widget = forms.TextInput(attrs={
            'class':'form-control',
            'id':'inputAddress',
            'placeholder':'1234 Main St',
        }))
    address2 = forms.CharField(label='Address 1',widget = forms.TextInput(attrs={
            'class':'form-control',
            'id':'inputAddress2',
            'placeholder':'Apartment, studio, or floor',
        }))

    city = forms.CharField(widget=forms.TextInput(attrs={
            'class':'form-control',
            'id':'inputCity',
        }))

    state = forms.ChoiceField(widget=forms.Select(attrs={
            'class':'form-control',
        }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'inputZip',
    }))
    check = forms.BooleanField(label = 'Check me out',initial=False,widget = forms.CheckboxInput(attrs={
        'class':'form-check-input',
        'id':'gridCheck',

    }))


    class Meta:
        model = CustomModel
        fields = '__all__'
