from django.db import models
from user_account.models import User

class UserProfile(models.Model):
    """All the required informations about the urser's partner"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    partner_name = models.CharField(max_length=100)
    partner_email = models.EmailField(max_length=254)
    partner_birthday = models.DateField()
    partner_nickname = models.CharField(max_length=100)
    partner_description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


class Date(models.Model):
    date = models.DateField()

class Schedule(models.Model):
    FREQUENCY_CHOICES = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    custom_dates = models.ManyToManyField(Date)

class LoveMessage(models.Model):
    """Generated message destinated to the user's partner."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    scheduled_date = models.DateField(Schedule)
    sent_date = models.DateField()
    sent = models.BooleanField(default=False)
