from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Audit(models.Model):
    """

    """
    # REQUEST_TYPE_POST = 'POST'
    # REQUEST_TYPE_GET = 'GET'
    # REQUEST_TYPE_PATCH = 'PATCH'
    # REQUEST_TYPE_DELETE = 'DELETE'
    # REQUEST_TYPE_PUT = 'PUT'
    #
    # REQUEST_TYPE_CHOICES = (
    #     (REQUEST_TYPE_POST, _('POST')),
    #     (REQUEST_TYPE_GET, _('GET')),
    #     (REQUEST_TYPE_PATCH, _('PATCH')),
    #     (REQUEST_TYPE_DELETE, _('DELETE')),
    #     (REQUEST_TYPE_PUT, _('PUT')),
    # )

    ACTIVITY_TYPE_LOGIN = 'LOGIN'
    ACTIVITY_TYPE_LOGOUT = 'LOGOUT'
    ACTIVITY_TYPE_PWD_RESET = 'PWD_RESET'
    ACTIVITY_TYPE_PWD_FORGOTTEN = 'PWD_FORGOTTEN'

    ACTIVITY_TYPE_CHOICES = (
        (ACTIVITY_TYPE_LOGIN, _('LOGIN')),
        (ACTIVITY_TYPE_LOGOUT, _('LOGOUT')),
        (ACTIVITY_TYPE_PWD_RESET, _('PWD_RESET')),
        (ACTIVITY_TYPE_PWD_FORGOTTEN, _('PWD_FORGOTTEN')),
    )

    description = models.CharField(
        verbose_name=_('Description'),
        max_length=255,
        blank=True,
        null=True
    )
    activity = models.CharField(
        verbose_name=_('Activity'),
        choices=ACTIVITY_TYPE_CHOICES,
        max_length=255,
        blank=True,
        null=True
    )
    request_type = models.CharField(
        verbose_name=_('Request type'),
        max_length=255,
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('User'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    ip_address = models.GenericIPAddressField(
        verbose_name=_('Ip address'),
        blank=True,
        null=True
    )
    user_agent = models.CharField(
        verbose_name=_('User agent'),
        max_length=255,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        blank=True,
        null=True,
        auto_now_add=True,
    )
