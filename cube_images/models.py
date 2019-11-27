# -*- coding: utf-8 -*-
from django.db import models
from .manager import CubeImagesManager


class Landscape(models.Model):
    panoramic = models.ImageField(upload_to='kebab')
    cubes = CubeImagesManager('panoramic')
