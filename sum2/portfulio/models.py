from django.db import models

class about(models.Model):
    name=models.CharField(max_length=100,blank=False)
    image=models.ImageField(upload_to='portfulio/',blank=False)
    def __str__(self):
        return self.name
