from django import forms

from memoreminder.models import MemoUser


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MemoUser
        fields = '__all__'