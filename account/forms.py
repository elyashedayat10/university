from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

user = get_user_model()


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = user
        fields = ("national_code", "name", "family")

    def clean_password_confirm(self):
        password1 = self.cleaned_data["password"]
        password2 = self.cleaned_data["password_confirm"]
        if password1 != password2:
            raise ValidationError("unmatch password")
        return password2

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = user
        fields = ("national_code", "name", "family", "password")


class AdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = user
        fields = ("national_code", "name", "family", "password")
    # password = forms.CharField(widget=forms.PasswordInput, label='رمز عبور')
    # national_code = forms.CharField(widget=forms.TextInput, label='کد ملی')
    # name = forms.CharField(widget=forms.TextInput, label='نام')
    # family = forms.CharField(widget=forms.TextInput, label='نام خانوادگی')


class LoginForm(forms.Form):
    national_code = forms.CharField(widget=forms.TextInput, label="کد ملی")
    password = forms.CharField(widget=forms.PasswordInput, label='رمزعبور')
