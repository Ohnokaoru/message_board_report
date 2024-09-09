from django import forms
from .models import BoardUnit, Comment
from captcha.fields import CaptchaField


class BoardUnitForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = BoardUnit

        fields = ("subject", "text")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ("text",)
