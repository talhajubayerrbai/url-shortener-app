from django.test import TestCase, Client
from django.urls import reverse
from .models import ShortURL


class ShortURLModelTest(TestCase):
    def test_code_generated_on_save(self):
        obj = ShortURL.objects.create(original_url='https://example.com')
        self.assertTrue(len(obj.code) >= 6)

    def test_code_unique(self):
        obj1 = ShortURL.objects.create(original_url='https://example.com/1')
        obj2 = ShortURL.objects.create(original_url='https://example.com/2')
        self.assertNotEqual(obj1.code, obj2.code)


class ShortURLViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_get(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Shorten')

    def test_shorten_post(self):
        response = self.client.post(reverse('index'), {'url': 'https://example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ShortURL.objects.count(), 1)

    def test_redirect(self):
        obj = ShortURL.objects.create(original_url='https://example.com')
        response = self.client.get(f'/{obj.code}')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], 'https://example.com')
        obj.refresh_from_db()
        self.assertEqual(obj.click_count, 1)

    def test_stats_page(self):
        obj = ShortURL.objects.create(original_url='https://example.com')
        response = self.client.get(reverse('stats', args=[obj.code]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, obj.code)

    def test_invalid_code_404(self):
        response = self.client.get('/doesnotexist')
        self.assertEqual(response.status_code, 404)
