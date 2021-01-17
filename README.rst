=============================
django-gitabix
=============================

.. image:: https://badge.fury.io/py/django-gitabix.svg
    :target: https://badge.fury.io/py/django-gitabix

.. image:: https://travis-ci.org/andytwoods/django-gitabix.svg?branch=master
    :target: https://travis-ci.org/andytwoods/django-gitabix

.. image:: https://codecov.io/gh/andytwoods/django-gitabix/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/andytwoods/django-gitabix

HHelp you remember what branch you're on

Documentation
-------------

The full documentation is at https://django-gitabix.readthedocs.io.

Quickstart
----------

Install django-gitabix::

    pip install django-gitabix

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_gitabix.apps.DjangoGitabixConfig',
        ...
    )

Add django-gitabix's URL patterns:

.. code-block:: python

    from django_gitabix import urls as django_gitabix_urls


    urlpatterns = [
        ...
        url(r'^', include(django_gitabix_urls)),
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


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
