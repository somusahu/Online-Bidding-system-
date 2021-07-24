from django.shortcuts import render,redirect
from django.http import HttpResponse
from Action_Platform.models import UserProfile
from .models import Compony,Product,bidding
from .models import Category
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def home(request):
	al=Product.objects.all()
	return render(request,"welcomeseller.html",{'pro':al})
def Componay(request):
	cobj = Compony.objects.all()
	if request.method == "POST":
		cname = request.POST['cn']
		cd = request.POST['cd']
		cl = request.POST['cl']
		uobj = User.objects.get(username=request.user)
		cobjs = Compony(compony_name=cname,details=cd,location=cl,user=uobj)
		cobjs.save()
		messages.success(request, "Compony added Successfully!")		
		return redirect('/seller/Componay/')		
		#return render(request,"<h2>Compony add sussfulley</h2>")
	return render(request,"add_componay.html",{'cat':cobj})

#======================================================================================

def add_product(request):
	cat1 = Category.objects.all()
	como= Compony.objects.all()
	if request.method =="POST":
		pn = request.POST['pn']
		pd = request.POST['pd']
		price = request.POST['mrp']
		img = request.FILES['pimg']
		upt = request.POST['time']
		end = request.POST['end']
		cat=request.POST['cat']
		com=request.POST['com']
	

		user = UserProfile.objects.get(user__username=request.user)
	
		proobj =Product(Product_name=pn,Product_details=pd,price=price,pro_img=img,updated_time=upt,end_time=end,category_id=cat,compony_id=com,user=user)
		proobj.save()

		messages.success(request, "Product added Successfully!")
		
	return render(request,"add_product.html",{'cat':cat1,'com':como})

#==============================================================================================================>
def category(request):
	cateobj = Category.objects.all()

	if request.method == "POST":
		catid = request.POST['cat']
		cateobjs = Category(category=catid)
		cateobjs.save()
		messages.success(request, "Category added Successfully!")

	return render(request,"category.html",{'cat':cateobj})

#=============================================================================================>
#def view_auction(request):

#	return render(request,"view_auction.html")
#----------------------------------------------------------
def bidding1(request): 
	userobj = UserProfile.objects.all()
	profileobj = User.objects.all()	
	data=[]
	for i in userobj:
		if i.usertype !='superAdmin' and i.usertype !='seller':
			print(i.usertype)
			data.append(i)
	return render(request,'bidding.html',{'data':data})
#============================================================
def Services(request):
	return render(request,"services.html")

#====================================================
def userdel(request,id):
	user=User.objects.get(id=id)
	user1=UserProfile.objects.get(user=user)
	user1.delete()
	user=User.objects.get(id=id)
	user.delete()

	return redirect('/seller/delete_user/')
#=================================================
def delete_bidder(request):
	user = UserProfile.objects.all()
	data=[]
	for i in user:
		if i.usertype !='seller':
			print(i.usertype)
			data.append(i)
	return render(request,"del_bidder.html",{'data':data})

def Contact_us(request):
	return render(request,"contact_us.html")
def Trems_and_Conditions(request):
	return render(request,"trems_conditions_s.html")
def help(request):
	return render(request,"help.html")

def bidder(request):
	proobj = Product.objects.all()
	print(pro)
	pro=[]
	pro.append(proobj)
	return render(request,"welcomeseller.html",{"pro":pro})

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
		email=y.user.email
		
		subject = 'varifiy bidding system'
		message = 'heppy birthday !'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [email,]
		send_mail( subject, message, email_from, recipient_list ) 
		return render(request,'win.html',{'pro':pro,'y':y})
	return render(request,'win.html',{'pro':pro})
