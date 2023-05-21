from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomerUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomerUser
        fields =  '__all__' # UserCreationForm.Meta.fields + ("name") 
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomerUser
        fields = '__all__' #UserChangeForm.Meta.fields +      