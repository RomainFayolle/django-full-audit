# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django_full_audit.urls', namespace='django_full_audit')),
    url(r'^', include('tests.apps.test_app.urls', namespace='test_app')),
]
