# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class conversionFactor(models.Model):
    unit = models.CharField(max_length=10)
    factor = models.FloatField()