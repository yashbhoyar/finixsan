from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=RichTextField()
    chart=models.ImageField(null=True,blank=True,upload_to="images/")
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

  
    def __str__(self):
        return self.title   
    
    
    #def get_absolute_url(self):
        #return reverse('post-detail',kwargs={'pk':self.pk})
    
    def get_absolute_url(self):
        return reverse('blog')