from django import forms
from .models import Post
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

"""
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError("Uzytkownik nie istnieje")

            if not user.check_password(password):
                raise forms.ValidationError("Niepoprawne haslo")

            if not user.is_active:
                raise forms.ValidationError("Konto zablokowane")
        return super(UserLoginForm, self).clean()
        """
