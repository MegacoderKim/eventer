from djnago.contrib.urls import url
from .views import (index,venue_detail,search)

urlpatterns = [
	url(r'^$',index,name='home'),
    url(r'^venue/(?P<slug>[-\w]+)',venue_detail,name='venue_detail'),
	url(r'^results/)',search,name='venue_search'),
]