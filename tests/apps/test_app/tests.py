from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from tests.apps.test_app.models import TestModel
from django_full_audit.models import Audit


class TestFullAuditMiddleware(TestCase):

    def setUp(self):
        self.username = 'George Abitbol'
        self.email = 'george@abitbol.com'
        self.password = 'pwd'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.client.login(username=self.username, password=self.password)

        self.browser = 'RandomBrowser/1.0'
        self.ip_address = '123.4.5.6'

    def test_create_object(self):
        create_sample_url = reverse('test_app:create-sample')
        self.client.post(
            create_sample_url,
            HTTP_USER_AGENT=self.browser,
            REMOTE_ADDR=self.ip_address)
        self.assertEqual(TestModel.objects.count(), 1)
        audits = Audit.objects.all()
        self.assertEqual(audits.count(), 1)
        self.assertEqual(audits[0].user, self.user)
        self.assertEqual(audits[0].request_type, 'POST')
        self.assertEqual(audits[0].user_agent, self.browser)
        self.assertEqual(audits[0].ip_address, self.ip_address)
