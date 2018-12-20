# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CaffeModel(models.Model):
    projectName = models.TextField()
    data = models.TextField()

    class Meta:
        db_table = "caffe_model"