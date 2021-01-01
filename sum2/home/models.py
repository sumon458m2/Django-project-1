from django.db import models

class section(models.Model):
    name=models.CharField(max_length=100,blank=False)
    description=models.TextField(max_length=500,blank=False)
    image=models.ImageField(upload_to='section/',blank=False)
    def __str__(self):
        return self.name
