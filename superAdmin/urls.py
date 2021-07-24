from django.urls import path
from . import views 
app_name='superAdmin'

urlpatterns = [
	path('home/',views.home),
	path('view_seller/',views.view_seller),
	path('delete_user/',views.delete_user),
	path('servies/',views.servies),
	path('treamconditions/',views.treamconditions),
	path('contact/',views.contact),


	path('del/<int:id>/',views.userdel,name='del')




	]
	
		