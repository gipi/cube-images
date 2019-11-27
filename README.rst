=============================
cube_images
=============================

.. image:: https://badge.fury.io/py/cube_images.svg
    :target: https://badge.fury.io/py/cube_images

.. image:: https://travis-ci.org/gipi/cube_images.svg?branch=master
    :target: https://travis-ci.org/gipi/cube_images

.. image:: https://codecov.io/gh/gipi/cube_images/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/gipi/cube_images

Store derived images in the filesystem.

Documentation
-------------

The full documentation is at https://cube_images.readthedocs.io.

Quickstart
----------

Install cube_images::

    pip install cube_images

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'cube_images.apps.CubeImagesConfig',
        ...
    )

Add cube_images's URL patterns:

.. code-block:: python

    from cube_images import urls as cube_images_urls


    urlpatterns = [
        ...
        url(r'^', include(cube_images_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
