from django.test import TestCase # type: ignore

class PortalHomepageTests(TestCase):
    def test_homepage_status_code(self):
        """Проверяем, что главная страница сайта отвечает статусом 200 (ОК)"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)