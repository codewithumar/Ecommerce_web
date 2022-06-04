from operator import imod
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import  MaxValueValidator,MinValueValidator

STATE_CHOICES =(
    ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands ' ),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh '),
    ('Assam',' ASsam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh ' ),
    ('Chhattisgarh', 'Chhattisgarh '),
    ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'),
    ('Daman and Diu', 'Daman and Diu'),)

class Customer (models.Model) :
    user =models.ForeignKey (User, on_delete=models .CASCADE) 
    name= models.CharField (max_length=30)
    locality = models.CharField (max_length=30)
    city =models.CharField (max_length=30)
    zipcode= models.IntegerField ()
    state=models.CharField(choices=STATE_CHOICES,max_length=30)

def  __str__(self):
    return str(self.id)

CATEGORY_CHOICES=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top wear'),
    ('BW','BottomWear'),
)
class Product (models.Model):
    title = models.CharField(max_length=30)
    selling_price = models.FloatField ()
    discounted_price = models.FloatField ()
    description = models.TextField ()
    brand =models.CharField (max_length=30)
    category = models.CharField (choices=CATEGORY_CHOICES,max_length=30)
    product_image = models.ImageField(upload_to='productimg')

def __str__(self):
    return str(self. id)



class Cart (models.Model):
    user =models.ForeignKey(User, on_delete=models. CASCADE)
    product= models.ForeignKey (Product, on_delete=models . CASCADE)
    quantity = models. PositiveIntegerField (default=1)


def __str__(self) :
    return str (self. id)


STATUS_CHOICES =(
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel' ))

class OrderPlaced (models.Model) :
    user =models.ForeignKey (User, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    product= models.ForeignKey (Product, on_delete=models.CASCADE)
    quantity = models. PositiveIntegerField (default=1)
    ordered_date = models . DateTimeField (auto_now_add=True)
    status = models.CharField (max_length=50,
    choices=STATUS_CHOICES, default='Pending')
# Create your models here.