from django import forms
from .models import BoardUnit
from captcha.fields import CaptchaField


class BoardUnitForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = BoardUnit

        fields = ("subject", "text")
