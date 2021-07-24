from django.db import models
from django.contrib.auth.models import User
from Action_Platform.models import UserProfile
# Create your models here.

class Compony(models.Model):
	compony_name = models.CharField(max_length=100)
	details = models.CharField(max_length=200)
	location = models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class Category(models.Model):
	category = models.CharField(max_length=150)

class Product(models.Model):
	Product_name = models.CharField(max_length=80)
	Product_details = models.CharField(max_length=200)
	price = models.DecimalField(decimal_places=2, max_digits=12)
	pro_img = models.ImageField(upload_to="product_image", blank=True)
	updated_time = models.DateTimeField(auto_now=True)
	end_time = models.DateTimeField(auto_now=True)
	compony = models.ForeignKey(Compony, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,default="10")

class views_Auction(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	status = models.CharField(max_length=50)

class bidding(models.Model):
	auction = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	price = models.DecimalField(decimal_places=2,max_digits=12)




