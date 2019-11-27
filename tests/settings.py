# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import django
import tempfile

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "ralz7^d!95i$v*%v+loc&w7app%2%h&vf(_b=o-sl1inruz=$9"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "cube_images",
]

SITE_ID = 1

TEST_TMP_DIR = tempfile.TemporaryDirectory()
MEDIA_ROOT = TEST_TMP_DIR.name
MEDIA_URL = '/media/'

if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()
