from django.db import models

# Create your models here.
class Post(models.Model):
    postName = models.CharField(max_length=120)
    featuredImage = models.ImageField(upload_to='media/')
    postContent = models.CharField(max_length=65535)