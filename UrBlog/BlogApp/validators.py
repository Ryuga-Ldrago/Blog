from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
 
def email_validation(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError(
            (f"{value} is already exist."),
            params={'value':value}
        )
