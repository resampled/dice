from django import forms
from captcha.fields import CaptchaField

class SignupWithCaptcha(forms.Form):
    captcha = CaptchaField()

    def save(self, request, user):
        user = super(SignupWithCaptcha, self).save(request)
        return user
    def signup(self, request, user):
        pass
