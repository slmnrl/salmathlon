from django.test import TestCase, Client
from main.models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    # Unit test apakah produk dapat dibuat dengan tepat
    def test_product_creation(self):
        s = Product.objects.create(name = "Skechers GOrun", amount = 10, description = "Advanced Cushioning Technology")
        self.assertTrue(isinstance(s, Product))
    