from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100) # membuat variable title dengan tipe data CharField, bisa dimasukkan max 100 character
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)