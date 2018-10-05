from django import forms
from register_user.models import User

class NewUserForm(forms.ModelForm):
    #insert validations here
    class Meta:
        model = User
        fields = '__all__'
