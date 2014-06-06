from django.db import models
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    """docstring for ClassName"""
    title = models.CharField(max_length=200)
    body = models.TextField()
    Created = models.DateTimeField()
    photo = models.ImageField(upload_to="image")
    tags = TaggableManager()

    class Meta:
        verbose_name_plural = "image"
    def __unicode__(self):
        return self.title

    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg

