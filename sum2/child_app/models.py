from django.db import models

class children(models.Model):
    title=models.CharField(max_length=100,blank=False)
    name=models.CharField(max_length=100,blank=False)
    description=models.TextField(max_length=1000,blank=False)
    image=models.ImageField(upload_to='section/',blank=False)
    
    def __str__(self):
        return self.title
class child(models.Model):
    name=models.CharField(max_length=100,blank=False)
    description=models.TextField(max_length=1000,blank=False)
    def __str__(self):
        return self.name



class testmonial(models.Model):
    title=models.CharField(max_length=100,blank=False)
    name=models.CharField(max_length=100,blank=False)
    description=models.TextField(max_length=1000,blank=False)
    image=models.ImageField(upload_to='testmonial/',blank=False)
    def __str__(self):
        return self.title

class team(models.Model):
    title=models.CharField(max_length=100,blank=False)
    name=models.CharField(max_length=100,blank=False)
    image=models.ImageField(upload_to='team/',blank=False)
    def __str__(self):
        return self.title