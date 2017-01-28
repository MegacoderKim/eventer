from django.conf.urls import url
from .views import (user_login,register) 

urlpatterns = [

	url(r'^login/$',user_login,name='login'),
	url(r'^register/$',register,name='register'),
			]