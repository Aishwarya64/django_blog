from django.db import models
from django.utils import timezone
from django.contrib.auth.models  import User
from django.urls import reverse
from django.db.models.signals import pre_save
from djan_1.utils import unique_slug_generator

# Create your models here.

class Post(models.Model) :
    title = models.CharField(max_length=100)
    context = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    def __self__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug':self.slug})
        #return 'post-detail',(),{'pk':self.pk}



    

def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)


pre_save.connect(slug_generator,sender=Post)