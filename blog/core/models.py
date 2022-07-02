from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=350)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    upload = models.ImageField(upload_to ='images/', null=True, blank=True)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author) + '  |  ' + str(self.date_added)