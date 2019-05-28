from django.test import TestCase, Client
from .views import index, getTypes, getProducts
from django.urls import reverse
from django.contrib.auth.models import User
from .models import TechType, Product, Review
from .forms import ProductForm
import datetime


# Create your tests here.
# Test for models.
class TechTypeTest(TestCase):
    def test_string(self):
        type=TechType(techtypename='laptop')
        self.assertEqual(str(type),type.techtypename)

    def test_table(self):
        self.assertEqual(str(TechType._meta.db_table),'techtype')

class ProductTest(TestCase):
    def setUp(self):
        self.type=TechType(techtypename='tablet')
        self.prod=Product(productname='Ipad', producttype=self.type, productprice=800.00)

    def test_string(self):
        self.assertEqual(str(self.prod),self.prod.productname)

    def test_type(self):
        self.assertEqual(str(self.prod.producttype),'tablet')

    def test_discount(self):
        self.assertEqual(self.prod.memberDiscount(),40.00)

#tests for views
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetProductsTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='myUser')
        self.type=TechType.objects.create(techtypename='laptop')
        self.prod=Product.objects.create(productname='product1', producttype=self.type, 
        user=self.u, productprice=500,productentrydate='2019-04-02', 
        productdescription='some kind of laptop')
    
    def test_product_detail_success(self):
        response=self.client.get(reverse('productdetails', args=(self.prod.id,)))
        self.assertEqual(response.status_code, 200)

# Form tests.
class Product_Form_Test(TestCase):    
# setup     
    def setUp(self):
        self.user=User.objects.create(username='myUser', password='P@ssw0rd1')
        self.type=TechType.objects.create(techtypename='type1')
         
    
# tests all fields filled
    def test_productform_is_valid(self):
        form=ProductForm(
            data={'productname':'product1', 
            'producttype':self.type, 
            'user':self.user, 
            'productprice':500.00,
            'productentrydate':'2019-05-28',
            'productentrydate':'https://github.com/', 
            'productdescription':'some kind of laptop'
            }
        )
        self.assertTrue(form.is_valid())

# tests fields excluding optional fields
    def test_productform_minus_descript(self):
        form=ProductForm(data={'productname': "type1", 'producttype' : "some type"
        ,'username' : "myUser",'productprice' : "100.00" , 'productentrydate' : "2019-05-16"
        ,'productdescription' : "some description"})
        self.assertTrue(form.is_valid())

# test fields empty
    def test_productform_empty(self):
        form=ProductForm(data={'productname': "", 'producttype' : ""
        ,'username' : "",'productprice' : "" , 'productentrydate' : "" 
        ,'productdescription' : ""})
        self.assertFalse(form.is_valid())