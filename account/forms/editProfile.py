from django.contrib.auth.forms import UserChangeForm
from django.forms import fields
from account.models import CustomUserModel

class editProfileForm(UserChangeForm):
    password=None
    class Meta:
        model = CustomUserModel
        fields = ('email','first_name','last_name','avatar')
