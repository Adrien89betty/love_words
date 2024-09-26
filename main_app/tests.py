from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import UserProfile
from datetime import date

User = get_user_model()

class UserProfileModelTest(TestCase):

    def setUp(self):
        # Create a user for all tests.
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )

        # Create UserProfile instance for all tests.
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            partner_name='Jane Doe',
            partner_email='jane.doe@example.com',
            partner_birthday=date(1990, 1, 1),
            partner_nickname='Sweetheart',
            partner_description='A wonderful person',
        )

    def test_user_profile_creation(self):
        # Checks that UserProfile object has been created correctly.
        self.assertEqual(self.user_profile.user, self.user)
        self.assertEqual(self.user_profile.partner_name, 'Jane Doe')
        self.assertEqual(self.user_profile.partner_email, 'jane.doe@example.com')
        self.assertEqual(self.user_profile.partner_birthday, date(1990, 1, 1))
        self.assertEqual(self.user_profile.partner_nickname, 'Sweetheart')
        self.assertEqual(self.user_profile.partner_description, 'A wonderful person')
        self.assertIsNotNone(self.user_profile.date_added)

