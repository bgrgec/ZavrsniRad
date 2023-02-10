from django.db import models

# Create your models here.

class Post(models.Model):
    postName = models.CharField(max_length=120)
    featuredImage = models.ImageField(upload_to='media/')
    postContent = models.CharField(max_length=65535)
    published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
class Author(models.Model):
    imeAutora = models.CharField(max_length=50)
    active = models.BooleanField(default=False)


class Category(models.Model):
    nazivKategorije = models.CharField(max_length=100)
    published = models.BooleanField(default=False)
