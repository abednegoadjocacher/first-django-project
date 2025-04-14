from django.db import models

# Create your models here.
class BlogPost(models.Model):
    name = models.CharField(max_length= 100)
    title = models.CharField(max_length=120)
    image_blog = models.ImageField(upload_to='images/')
    message = models.TextField(max_length= 5000)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} by {self.name}"