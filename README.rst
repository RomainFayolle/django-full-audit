=============================
django-full-audit
=============================

.. image:: https://badge.fury.io/py/django_full_audit.svg
    :target: https://badge.fury.io/py/django_full_audit

.. image:: https://travis-ci.org/RomainFayolle/django_full_audit.svg?branch=master
    :target: https://travis-ci.org/RomainFayolle/django_full_audit

.. image:: https://codecov.io/gh/RomainFayolle/django_full_audit/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/RomainFayolle/django_full_audit

Your project description goes here

Documentation
-------------

The full documentation is at https://django_full_audit.readthedocs.io.

Quickstart
----------

Install django-full-audit::

    pip install django_full_audit

Add it to your `INSTALLED_APPS`:

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

Features
--------
This project aim to:
* Log all API requests
* Log all logins, logouts, and password changes/resets
* Indicate IP address, date, User, type of request and web browser version

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
