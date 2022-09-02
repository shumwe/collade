from django.test import TestCase
from accounts.models import Profile
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.tester1 = User.objects.create(
            username="tester",email="tester@mail.com",first_name="tester",
            last_name="one",avatar="avatars/bravin/its_me.jpg",
        )
    
    def test_check_user_is_created(self):
        get_tester = User.objects.get(username=self.tester1.username)
        self.assertEqual(get_tester.username, 'tester')
        
    def test_chack_profile_is_created(self):
        profile = Profile.objects.get(
            user=self.tester1
        )
        self.assertEqual(profile.user, self.tester1)