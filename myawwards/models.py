from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver

# Create your models here.
class Projects(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='projects/')
    design=models.IntegerField(default=0)
    usability=models.IntegerField(default=0)
    content=models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField(max_length=320)
    link=models.URLField(max_length=60)
    date=models.DateField(auto_now=True)
    
    class Meta:
        ordering=['-name']

    def __str__(self):
        self.name

    @classmethod
    def search_project(cls,word):
        searched=cls.objects.filter(name__icontains=word)
        return searched

    def delete_project(self):
        self.delete()
    
    @classmethod
    def all_projects(cls):
        return cls.objects.all()

    def save_project(self):
        self.save()



class Profile(models.Model):
    profile=models.ImageField(upload_to='profile/')
    bio=models.CharField(max_length=60)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    class Meta:
        ordering=['-profile']

    
   

class Rates(models.Model):
    design=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    usability=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    content=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.IntegerField(default=0)

    def save_rate(self):
        self.save()
