from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import EmailUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        # fields = UserCreationForm.Meta.fields + ('site',)
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields

# class SocialGoogleForm(forms.Form):
#     id_token = forms.CharField(widget=forms.Textarea, required=True, )
