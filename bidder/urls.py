from django.urls import path
from . import views
app_name='bidder'
urlpatterns =[
	path('home/',views.home),
	path('product_info/<int:id>',views.product_info,name='pro'),
	path('bid/',views.bid),
	path('contact/',views.contact),
	path('video/',views.video),
	path('about/',views.about),
	path('search/',views.search)

]

