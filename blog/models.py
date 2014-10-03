# -*- coding: utf-8 -*-
import django.db.models.options as options
from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
  # https://docs.djangoproject.com/en/1.4/glossary/
  title = models.CharField(max_length=255)
  slug = models.SlugField(unique=True, max_length=255) #  A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.
  description = models.CharField(max_length=255)
  content = models.TextField()
  published = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True)

  class Meta: # should be inside of your Model.
    # Fix : TypeError: 'class Meta' got invalid attribute(s): get_absolute_url -> http://stackoverflow.com/questions/1088431/adding-attributes-into-django-models-meta-class    
    # options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('get_absolute_url',)    
    
    ordering = ['-created'] # ordered by 'created' in descending order. "-" means descending order

    # Note : 'Model' base provides automatically a __str__() implementation that calls __unicode__()

    def __unicode__(self): # returns a unicode object - You'll normally use 
      return u'%s' % self.title

    def get_absolute_url(self):
      return reverse('blog.views.post', args=[self.slug])
