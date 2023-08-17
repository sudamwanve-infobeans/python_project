from django import forms
from django.contrib.auth.models import User
from ecom.models import UserProfileInfo,BlogModel,Product,Orders

# created user registration form using ModelForm
class UserForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


# To add extra field: profile_pic
class UserProfileInfoForm(forms.ModelForm):

    class Meta():

        model = UserProfileInfo
        fields = ('profile_pic','address')
        widgets = {
            'address': forms.Textarea(attrs={'rows': 5, 'cols': 20})
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields=['status']

class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)


