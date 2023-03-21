from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES=(
    ('CR','Curd'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('MS','MilkShake'),
    ('PN','Paneer'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
    ('IC','Ice-Creams'),
)

STATE_CHOICES=(
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'), 
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'), 
    ('Himachal Pradesh','Himachal Pradesh'), 
    ('Jammu and Kashmir','Jammu and Kashmir'),  
    ('Jharkhand ','Jharkhand '),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'), 
    ('Madhya Pradesh','Madhya Pradesh'),  
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'), 
    ('Meghalaya','Meghalaya'), 
    ('Mizoram','Mizoram'), 
    ('Nagaland','Nagaland'), 
    ('Odisha','Odisha'), 
    ('Punjab','Punjab'), 
    ('Rajasthan','Rajasthan'), 
    ('Sikkim','Sikkim'), 
    ('Tamil Nadu ','Tamil Nadu '),
    ('Telangana ','Telangana '), 
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal')
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name