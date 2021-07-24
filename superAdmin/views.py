from django.shortcuts import render
from Action_Platform.models import UserProfile
from django.contrib.auth.models import User



# Create your views here.
def home(request):
	return render(request,"wc.html")

def view_seller(request):
	userobj = UserProfile.objects.all()
	profileobj = User.objects.all()	
	data=[]
	for i in userobj:
		if i.usertype !='superAdmin':
			print(i.usertype)
			data.append(i)
	return render(request,'user_type.html',{'data':data})

def delete_user(request):
	user = UserProfile.objects.all()
	data=[]
	for i in user:
		if i.usertype !='superAdmin':
			print(i.usertype)
			data.append(i)


	return render(request,"delete_user.html",{'data':data})

def userdel(request,id):
	user=User.objects.get(id=id)
	user1=UserProfile.objects.get(user=user)
	user1.delete()
	user=User.objects.get(id=id)
	user.delete()

	return redirect('/superAdmin/delete_user/')

	return render(request,"wc.html")


def servies(request):
	return render(request,'services.html')

def treamconditions(request):
	return render(request,'trems_conditions_s.html')

def contact(request):
	return render(request,'contact.html')
	
