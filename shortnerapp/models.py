from __future__ import unicode_literals

from django.db import models

import hashlib

# Create your models here.

class UrlMapper(models.Model):
    long_url = models.CharField(max_length=1000,null=True,blank=True)
    short_url = models.CharField(max_length=1000,null=True,blank=True)




