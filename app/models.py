# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Comment(models.Model):
    id  = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    n_visits = models.IntegerField()

    def __str__(self):
        return self.headline

class UserInfo(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()
	memo = models.TextField()
