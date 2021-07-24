from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	usertype = models.CharField(max_length=50)
	mobile = models.CharField(max_length=12)
	address= models.CharField(max_length=100)

class Profile(models.Model):
	puser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	auth_token = models.CharField(max_length=100)
	is_verified = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.puser.username


