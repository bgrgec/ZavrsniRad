from django.db import models
import datetime

class Author(models.Model):
    imeAutora = models.CharField(max_length=50)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.imeAutora

class Category(models.Model):
    nazivKategorije = models.CharField(max_length=100)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.nazivKategorije


class Post(models.Model):
    postName = models.CharField(max_length=120, default='')
    featuredImage = models.ImageField(upload_to='images/', default='')
    postContent = models.TextField(default='')
    datePublished = models.DateField(default=datetime.date.today())
    published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.postName


        