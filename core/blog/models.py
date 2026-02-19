from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

# getting user model object
User = get_user_model()


class Post(models.Model):
    '''
    This is a class to define posts for blog app
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    image = models.ImageField(upload_to='images/post', null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
