from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormPendaftaran(UserCreationForm):
    n_phone = forms.IntegerField()

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'email',
            'n_phone',
        ]

    # def seve(self, commit=True):
    #     user = super(FromPendaftaran, self).seve(commit=False)
    #     user.n_phone = self.clean_data['n_phone']
    #     if commit:
    #         user.save()
    #     return user




