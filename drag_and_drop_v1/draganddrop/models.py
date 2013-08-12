from django.db import models

# Create your models here.

class UploadForm(models.Model):
    name = models.CharField(max_length = 250)
    email = models.EmailField(max_length = 250)
    phone = models.CharField(max_length = 250)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    
    def __unicode__(self):
        return self.email
    
