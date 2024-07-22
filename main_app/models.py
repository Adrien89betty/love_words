from django.db import models
from user_account.models import User

class UserProfile(models.Model):
    """All the required informations about the urser's partner"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    partner_name = models.CharField(max_length=100)
    partner_email = models.EmailField(max_length=254)
    partner_birthday = models.CharField
    partner_nickname = models.CharField
    partner_description = models.CharField
    date_added = models.DateTimeField(auto_now_add=True)

