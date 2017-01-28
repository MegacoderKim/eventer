from django.db import models
from django.core.urlresolvers import reverse

class Facility(models.Model):
    """
        The faclilities offered by the venue eg Wifi, Projectors, Food and Beverage etc
    """
    name = models.CharField(max_length=10,blank=False)
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'facility'
        verbose_name_plural = 'facilities'

    def __unicode__(self):
        return self.name

# Create your models here.
class Venue(models.Model):
    """
        This is a space listing for the database
    """
    EVENT_TYPE = (('HOT','HOTEL'),
                  ('REST','RESTAURANT'),
                  ('RES','RESORT'),
                  ('SPCS','SPORTS CENTER'),
                  ('ACAD','ACADEMIC CENTER')
                  )
    slug = models.SlugField(unique=True,)
    name = models.CharField(max_length= 200,blank=False)
    contact = models.CharField(max_length=200,)
    eventype = models.CharField(max_length=5,choices=EVENT_TYPE)
    description = models.CharField(max_length=200,)
    facilities = models.ManyToManyField(Facility,related_name='venue_facility')
    feature_photo = models.ImageField(upload_to="media/featured", blank=False,default="radisson.jpg")
    address = models.CharField(max_length=200,)
    created = models.DateTimeField(auto_now_add=True,)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):

        return reverse('venue_detail',args=[self.slug])



class Photo(models.Model):
    """
        Photos instance for the database
    """
    slug = models.SlugField(max_length=20, unique=True)
    #image = models.ImageField(upload_to="photos/", blank=False)#dev:sick windows
    image = models.ImageField(upload_to="photos/%Y/%m/%d",blank=False)#prod:since windows Sucks
    venue = models.ForeignKey(Venue,related_name='venue_photo')
    featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True,)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.slug
