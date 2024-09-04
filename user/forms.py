from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField


# AuthenticationForm已含帳密
class ChaloginForm(AuthenticationForm):
    captcha = CaptchaField()
