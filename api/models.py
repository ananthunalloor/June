from __future__ import unicode_literals
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150,blank=False,null=False)
    overview = models.TextField(default="Small description",max_length=250, blank=True)
    description = models.TextField(default="Detailed description",max_length=1500, blank=True)
    category = models.CharField(max_length=60,blank=True,null=True)
    added_date = models.DateField(auto_now=True,name="added date")
    added_time = models.TimeField(auto_now=True,name="added time")
    slug = models.SlugField(unique=True, default="thisisaslug")

    def save(self, *args, **kwargs):
        import random
        key = random.randint(1,702550)
        slug_key = str(self.title) +"-"+ str(key)
        self.slug = slugify(slug_key)
        super(Project, self).save(*args, **kwargs)