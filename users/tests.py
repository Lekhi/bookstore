from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='lekhi',
            email='lekhi@gmail.com',
            password='testpass1234',
        )
        self.assertEqual(user.username, 'lekhi')
        self.assertEqual(user.email, 'lekhi@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='adminho',
            email='adminho@email.com',
            password='testadminpassword2136',
        )
        self.assertEqual(admin_user.username, 'adminho')
        self.assertEqual(admin_user.email, 'adminho@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

