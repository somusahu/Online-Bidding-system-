from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import UserProfile
from django.contrib.auth import authenticate, login ,logout


def home(request):
	return render(request,"welcomebidder.html")
	
def signup_call(request):
	if request.method =="POST":
		fn = request.POST['fname']
		ln = request.POST['lname']
		un = request.POST['uname']
		pwd = request.POST['password']
		em = request.POST['email']
		mob = request.POST['mobile']
		addr = request.POST['address']
		type = request.POST['type']

		uobj =User(first_name=fn,last_name=ln,username=un,password=make_password(pwd),email=em)
		uobj.save()

		user_pro_obj =UserProfile(user=uobj,usertype=type,mobile=mob,address=addr)
		user_pro_obj.save()

	return render(request,"signup.html")

def login_call(request):
	if request.method =="POST":
		un = request.POST['uname']
		pwd = request.POST['password']

		user = authenticate(username=un,password=pwd)
		if user:
			login(request,user)
			profileobj = UserProfile.objects.get(user__username=request.user)
			if profileobj.usertype == "superAdmin":
				return redirect('/superAdmin/home/')

			elif profileobj.usertype == "seller":
				return redirect('/seller/home/')

			elif profileobj.usertype =="bidder":
				return redirect('/bidder/home/')

		else:
			return HttpResponse("<h1>Invalid Credentials</h1>")



	return render(request,"login.html")
def logout_call(request):
	logout(request)
	return redirect('/login/')



