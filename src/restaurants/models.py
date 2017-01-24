from __future__ import unicode_literals

from django.db import models


class Restaurant(models.Model):
    name = models.CharField(blank=False, max_length=50, unique=True)
    logo = models.ImageField(blank=False, upload_to='logos/')
    opening_from = models.TimeField(blank=False, verbose_name='Open from')
    opening_to = models.TimeField(blank=False, verbose_name='Open to')

    def __unicode__(self):
        return self.name
