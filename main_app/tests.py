from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import UserProfile, LoveMessage
from datetime import date

User = get_user_model()

class BaseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Creates User instance.
        cls.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password=" testpass123"
        )

    def create_user_profile(
        self,
        partner_name,
        partner_email,
        partner_birthday,
        partner_nickname,
        partner_description,
    ):
        # Creates UserProfile instance.
        return UserProfile.objects.create(
            user=self.user,
            partner_name=partner_name,
            partner_email=partner_email,
            partner_birthday=partner_birthday,
            partner_nickname=partner_nickname,
            partner_description=partner_description,
        )

    def create_love_message(self, content, scheduled_date, sent_date, sent=False):
        # Creates LoveMessage instance.
        return LoveMessage.objects.create(
            user=self.user,
            content=content,
            scheduled_date=scheduled_date,
            sent_date=sent_date,
            sent=sent,
        )

class UserProfileModelTest(BaseModelTest):
    def test_user_profile_creation(self):
        # Checks that UserProfile object has been created correctly.
        profile = self.create_user_profile(
            partner_name="Flore",
            partner_email="flore.betty@example.com",
            partner_birthday=date(1990, 11, 7),
            partner_nickname="Betty",
            partner_description="A wonderful person",
        )
        self.assertEqual(profile.partner_name, "Flore")
        self.assertEqual(profile.partner_email, "flore.betty@example.com")
        self.assertEqual(profile.partner_birthday, date(1990, 11, 7))
        self.assertEqual(profile.partner_nickname, "Betty")
        self.assertEqual(profile.partner_description, "A wonderful person")

class LoveMessageModelTest(BaseModelTest):
    def test_love_message_creation(self):
        love_message = self.create_love_message(
            content="You are fantastic!",
            scheduled_date=date(2024, 10, 1),
            sent_date=date(2024, 10, 1),
            sent=True,
        )
        self.assertEqual(love_message.content, "You are fantastic!")
        self.assertEqual(love_message.scheduled_date, date(2024, 10, 1))
        self.assertEqual(love_message.sent_date, date(2024, 10, 1))
        self.assertTrue(love_message.sent)

    def test_love_message_default_sent_value(self):
        love_message = self.create_love_message(
            content="You are awesome!",
            scheduled_date=date(2024, 12, 25),
            sent_date=date(2024, 12, 26),
        )
        self.assertFalse(love_message.sent)

class ScheduleModelTest(BaseModelTest):
    def test_schedule_creation(self):
        pass
