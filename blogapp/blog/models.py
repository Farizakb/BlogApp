from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(default ="",blank = True, unique=True, db_index = True)
    
    def __str__(self) -> str:
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to = "blogs")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(default ="",blank = True, unique=True, db_index = True)
    catagories = models.ManyToManyField(Catagory, related_name = "blog")    
    
    def __str__(self) -> str:
        return self.title

