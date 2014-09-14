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
    ordering = ['-created'] # ordered by 'created' in descending order. "-" means descending order

    # Note : 'Model' base provides automatically a __str__() implementation that calls __unicode__()

    def __unicode__(self): # returns a unicode object - You'll normally use 
      return u'%s' % self.title

    def get_absolute_url():
      return reverse('blog.views.post', args=[self.slug])