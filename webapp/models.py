from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.
class tags(models.Model):

    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name

  
class posts(models.Model):
    headline = models.CharField( max_length=50)
    sub_headline = models.CharField( max_length=250)
    thumbnail= models.ImageField(null=True , blank=True , default='1691219476696.jpg')
    body = models.TextField(null=True , blank=True)
    created = models.DateTimeField( auto_now_add=True)
    tags=models.ManyToManyField(tags, null=True)
 
    def __str__(self):
        return self.headline

   