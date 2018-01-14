from registration.forms import RegistrationForm

from diamond.models import CustomUser


class MyCustomUserForm(RegistrationForm):
    class Meta:
        model = CustomUser
        fields = ('phone', 'skype', 'country', 'city', 'birthdate', 'date_joined')
