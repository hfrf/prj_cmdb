# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    sex = models.CharField(default='male',max_length=10)