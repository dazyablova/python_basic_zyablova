from django.test import TestCase
from models import Category, Product
from django.urls import reverse

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', description='Test Description')

    def tearDown(self):
        self.category.delete()

    def test_category_name(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.name, 'Test Category')

    def test_category_description(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.description, 'Test Description')

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', description='Test Description')
        self.product = Product.objects.create(name='Test Product', description='Test Description', price=10.00, category=self.category)

    def tearDown(self):
        self.product.delete()
        self.category.delete()

    def test_product_name(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.name, 'Test Product')

    def test_product_description(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.description, 'Test Description')

    def test_product_price(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.price, 10.00)

    def test_product_category(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.category, self.category)

class CategoryListViewTest(TestCase):
    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/category_list.html')

class ProductDetailViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', description='Test Description')
        self.product = Product.objects.create(name='Test Product', description='Test Description', price=10.00, category=self.category)

    def tearDown(self):
        self.product.delete()
        self.category.delete()

    def test_product_detail_view(self):
        response = self.client.get(reverse('product_detail', kwargs={'pk': self.product.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')