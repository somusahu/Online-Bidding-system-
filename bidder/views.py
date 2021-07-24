from django.shortcuts import render,redirect
from seller.models import Compony,Category,Product,bidding
import datetime
from seller.models import bidding,views_Auction
from django.contrib.auth.models import User
from django.contrib import messages
from Action_Platform.models import UserProfile
from django.db.models import Q


# Create your views here.
def home(request):
	comobj = Compony.objects.all()
	catobj = Category.objects.all()
	proobj = Product.objects.all()
	p=print(datetime.datetime.today())

	return render(request,"welcomebidder.html",{"comobj":comobj, "catobj":catobj, "proobj":proobj})

def product_info(request,id):
	comobj = Compony.objects.all()
	catobj = Category.objects.all()
	proobj = Product.objects.get(id=id)
	#user = UserProfile.get(id=id)

	return render(request,"product_info.html",{"comobj":comobj,"catobj":catobj, "i":proobj})
	


def bid(request):
	so=request.POST['Pr']
	price=request.POST['pric']
	user = User.objects.get(username=request.user)
	p=Product.objects.get(id=so)
	c=bidding(auction=p,price=price,user=user)
	c.save()
	print(c)
	messages.success(request,"your bidding is  Successfully ! plise")

	return redirect('/bidder/home/')


def contact(request):
	return render(request,"BidContact.html")

def video(request):
	return render(request,"videos.html")

def about(request):
	return render(request,"about.html")

def win(request):
	pro=Product.objects.all()
	if request.method== 'POST':
		dp=request.POST['somu']
		b=bidding.objects.filter(auction__id=dp)
		x=0
		y=[]
		for i in b:
			if i.price>x:
				x=i.price 
				#{{i.user.username}}
				y=i
		return render(request,'win.html',{'pro':pro,'y':y})
	return render(request,'win.html',{'pro':pro})


def search(request):
	comobj = Compony.objects.all()
	catobj = Category.objects.all()
	proobj = Product.objects.all()
	p=print(datetime.datetime.today())

	q = request.POST['q']
			
	proobj = Product.objects.filter(Product_name=q)
	return render(request,"welcomebidder.html",{"comobj":comobj, "catobj":catobj, "proobj":proobj})
