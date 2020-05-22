from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

MODEL = get_user_model()
USERNAME_FIELD = MODEL.USERNAME_FIELD if hasattr(MODEL,'USERNAME_FIELD') else 'username'

class PasswordlessAuthBackend(ModelBackend):
    def authenticate(self, username=None):
        try:
            return MODEL.objects.get(**{USERNAME_FIELD:username})
        except MODEL.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return MODEL.objects.get(pk=user_id)
        except MODEL.DoesNotExist:
            return None
