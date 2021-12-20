from django.forms import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm:
    password = forms.CharField(min_length=6,
                               widget=forms.PasswordInput
                               )
    password_confirm = forms.CharField(min_length=6,
                                        widget=forms.PasswordInput
                                       )

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password_confirm']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Этот email уже занят')
        return email

    def clean(self):
        data = self.clean_data
        password = data.get('password')
        password2 = data.pop('password_confirm')
        if password != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return data

    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(**data)
        user.create_activation_code()
        #TODO: отправка на почту
        return user





class ActivationForm:
    pass


class LoginForm:
    pass


class ChangePasswordForm:
    pass


class ForgotPasswordForm:
    pass
