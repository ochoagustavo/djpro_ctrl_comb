from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    def test_crear_usuario(self):
        Usr = get_user_model()
        usr = Usr.objects.create_user(
            username = "debsconsultores",
            email = "debsconsultores@gmail.com",
            password = "123"
        )

        self.assertEqual(usr.username,"debsconsultores")
        self.assertEqual(usr.email,"debsconsultores@gmail.com")
        self.assertTrue(usr.is_active)
        self.assertFalse(usr.is_staff)
        self.assertFalse(usr.is_superuser)

