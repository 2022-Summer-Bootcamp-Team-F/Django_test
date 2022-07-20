from pyexpat import model
from django.db import models
from django.utils.timezone import datetime

class Image_URL(models.Model):
    image_id = models.BigAutoField(primary_key=True)
    pub_date = models.DateTimeField('date published', default=datetime.now, editable=False)
    image_url = models.CharField(max_length=100)
    