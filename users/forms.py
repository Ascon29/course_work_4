from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from newsletter.forms import StyleForm
from users.models import User


class UserRegisterForm(StyleForm, UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email",
            "phone_number",
            "avatar",
            "country",
            "password1",
            "password2",
        )

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number and not phone_number.isdigit():
            raise ValidationError("Номер телефона должен содержать только цифры")
        return phone_number


class UserUpdateForm(StyleForm, ModelForm):
    class Meta:
        model = User
        fields = (
            "phone_number",
            "avatar",
            "country",
        )

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number and not phone_number.isdigit():
            raise ValidationError("Номер телефона должен содержать только цифры")
        return phone_number
