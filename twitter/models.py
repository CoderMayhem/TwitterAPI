from django.db import models

# Create your models here.


class Tweet(models.Model):

    tweet = models.CharField(max_length=140, default = 'Default tweet') 
