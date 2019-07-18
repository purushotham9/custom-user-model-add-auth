from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = MyUser
        fields = ('id', 'email', 'password', 'first_name', )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = MyUser
        fields = UserChangeForm.Meta.fields