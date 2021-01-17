=====
Usage
=====

To use django-gitabix in a project, add it to your `INSTALLED_APPS`:

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
