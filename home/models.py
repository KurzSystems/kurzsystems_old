from django.db import models

from wagtail.core.models import Page
from cloudinary.models import CloudinaryField

class HomePage(Page):
    pass

class NotifyEmail(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
# temporarily store coming soon video while implementing cloudinary
class Video(models.Model):
  video = CloudinaryField('video', resource_type='video', null=True)
  


