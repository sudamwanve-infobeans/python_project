from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # additional field to add :
    address = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return  self.user.username



# Galery Model
class BlogModel(models.Model):

    desc            = models.TextField()
    blog_img     = models.ImageField(upload_to='blog', blank=False)
    userid          = models.ForeignKey(User, related_name='user', null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('ecom:my_blog')
    
    def __str__(self):
        return self.desc

class Product(models.Model):
    name = models.CharField(max_length=40)
    product_image = models.ImageField(upload_to='product_image/', null=True, blank=True)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=40)

    def get_absolute_url(self):
        return reverse('ecom:my_blog')

    def __str__(self):
        return self.name

class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    userid = models.ForeignKey(User, related_name='Customer', null=True, on_delete=models.CASCADE)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)
