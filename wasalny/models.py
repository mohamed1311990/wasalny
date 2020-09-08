# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

def upload_photo(self, filename):
    path = '/wasalny/photo/{}'.format(filename)
    return path
class Users(models.Model):
    employee_id = models.IntegerField(blank=True)
    name = models.CharField(blank=True,max_length=40)
    email = models.EmailField(blank=True,max_length=40)
    password = models.CharField(blank=True,max_length=40)
    password2 = models.CharField(blank=True,max_length=40)


    profile_photo = models.ImageField(upload_to=upload_photo, null=True, blank=True)

    def __str__(self):
        return format(self.name)