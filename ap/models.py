from django.db import models

# Create your models here.
class user(models.Model):
    f_name: models.CharField(max_length=100)
    l_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    gender=models.CharField(max_length=20)
    email=models.CharField(max_length=100)
    phone=models.IntegerField()
    
class male(models.Model):
    email=models.CharField(max_length=100)
    favourite_game=models.CharField(max_length=100)
    favourite_sports_person=models.CharField(max_length=100)
class female(models.Model):
    email=models.CharField(max_length=100)
    favourite_color=models.CharField(max_length=100)
    favourite_beauty_brand=models.CharField(max_length=100)
    favourite_beauty_product=models.CharField(max_length=100)
