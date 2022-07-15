from pyexpat import model
from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=30)
    image = models.FileField(upload_to='media/', blank=True)

    def __str__(self):
        return self.name

class Image_URL(models.Model):
    pub_date = models.DateTimeField('date published', default=datetime.now, editable=False)
    image_url = models.CharField(max_length=100)