
from .models import Account
from django.contrib.auth.backends import BaseBackend


class AccountLoginBackend(BaseBackend):
    def authenticate(self, request, username=None, contact=None, password=None,):
        try:
            user = None
            if contact is not None:
                user = Account.objects.get(contact=contact)
            elif username is not None:  # for loging in from django admin  anel
                user = Account.objects.get(username=username)

            if user is not None and user.check_password(password):
                return user

        except Account.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return Account.objects.get(pk=user_id)
        except Account.DoesNotExist:
            return None
