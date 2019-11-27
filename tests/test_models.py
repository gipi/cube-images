#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tempfile
from django.test import TestCase
from django.core.files import File
from django.core.files.base import ContentFile
from cube_images import models


class TestCube_images(TestCase):

    def setUp(self):
        pass

    def test_something(self):
        model = models.Landscape.objects.create(panoramic=ContentFile('ciao'))
        content = ContentFile(b'ciao')
        model.panoramic.save('viao.txt', content)
        model.save()

        print(f'{model.panoramic.name} {model.panoramic.path} {model.panoramic.url}')
        print(model.cubes.tile_f)
        print(f'{model.cubes.tile_f.path} {model.cubes.tile_f.url}')

    def tearDown(self):
        pass
