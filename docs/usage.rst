=====
Usage
=====

To use django-full-audit in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_full_audit.apps.DjangoFullAuditConfig',
        ...
    )

Add django-full-audit's URL patterns:

.. code-block:: python

    from django_full_audit import urls as django_full_audit_urls


    urlpatterns = [
        ...
        url(r'^', include(django_full_audit_urls)),
        ...
    ]
