from django.db import models

class MapImage(models.Model):

    slug = models.SlugField(max_length=255, unique=False, verbose_name='slug')
    ground_flour = models.ImageField(upload_to='map_output/')
    first_flour = models.ImageField(upload_to='map_output/')
    second_flour = models.ImageField(upload_to='map_output/')

