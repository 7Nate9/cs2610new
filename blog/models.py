# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime

from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=200)
    auth_name = models.CharField(max_length=50)
    content = models.CharField(max_length=25000)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.content