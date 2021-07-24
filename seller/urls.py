from django.urls import path
from . import views 

urlpatterns = [
	path('home/',views.home),
	path('Componay/',views.Componay),
	path('add_product/',views.add_product),
	path('category/',views.category),
	path('bidding/',views.bidding1),
	path('Services/',views.Services),
	path('Contact_us/',views.Contact_us),
	path('Trems_and_Conditions/',views.Trems_and_Conditions),
	path('help/',views.help),
	path('win/',views.win)
	#path('delete_user/',views.delete_bidder),

#	path('del/<int:id>/',views.userdel,name='del')



	]
	
		