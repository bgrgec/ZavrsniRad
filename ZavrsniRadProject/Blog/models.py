from django.db import models

# Create your models here.
class Author(models.Model):
    imeAutora = models.CharField(max_length=50)
    active = models.BooleanField(default=False)


class Category(models.Model):
    nazivKategorije = models.CharField(max_length=100)
    published = models.BooleanField(default=False)


class Post(models.Model):
    naslovObjave = models.CharField(max_length=200)
    objavaContent = models.CharField(max_length=65535)
    published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)