from django import forms
from user_app.models import Users

class NewUserForm(forms.ModelForm):
    class Meta():
        model = Users
        fields = "__all__"