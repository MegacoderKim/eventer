from django.shortcuts import render,get_object_or_404
from .models import Venue,Photo

# Create your views here.
def index(request):
	slider = Photo.objects.filter(featured= True) # will implements a slider logic later in markerting app
	featured_venue = Venue.objects.all()[:3]# crazy login to get the first three events
	template = 'venue/index.html'
	#template = 'test.html'# no css view database results
	context = {'slider':slider,'feature':featured_venue}

	return render(request,template,context)

def venue_detail(request,slug):
	the_venue = get_object_or_404(Venue,slug=slug)
	venue_images = Photo.objects.filter(venue__slug=slug)
	template = "venue/venue_detail.html"
	context = {'venue':the_venue,'images':venue_images,}

	return render(request,template,context)

def search(request,name = None,descrip = None, event_type = None):

	results = Venue.objects.filter(name__icontains = name, 
		description__icontains =descrip, event_type = event_type)

	template = 'venue/listing.html'
	context = {'results':results,}
	return render(request,template,context)



