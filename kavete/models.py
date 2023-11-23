import os.path
import uuid

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser

from user_profiles.models import UserProfile


# Create your models here.
def unique_image_name(instance, filename):
    name = uuid.uuid4()
    extension = filename.split('.')[-1]
    fullname = f'{name}.{extension}'
    return os.path.join('blog_post_images', fullname)


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    category_choices = [
        ('arduino', 'Arduino'),
        ('electronics', 'Electronics'),
        ('linux', 'Linux'),
        ('literature', 'Literature'),
    ]
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=category_choices)
    content = RichTextUploadingField(unique=True)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    preview_image = models.ImageField(upload_to=unique_image_name, null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.title} by {self.author}'
