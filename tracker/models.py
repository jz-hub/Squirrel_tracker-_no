from django.db import models
from django.utils.translation import gettext as _


class squirrel(models.Model):
    latitude = models.DecimalField(
        help_text = 'Latitude of sighting point',
        max_digits = 20,
        decimal_places = 10,
    )

    longitude = models.DecimalField(
        help_text = 'Longitude of sighting point',
        max_digits = 20,
        decimal_places = 10,
    )


    unique_squirrel_id = models.CharField(
        help_text = 'Unique ID number',
        max_length = 30,
        primary_key = True,
    )   

    date = models.DateField(
        help_text = 'date',
        max_length = 20,
    )
    
# Create your models here.
