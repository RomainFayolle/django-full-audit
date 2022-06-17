from django_full_audit.models import Audit


class FullAuditMiddleware(object):
    """

    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        log_data = {}
        if request.user:
            log_data['user'] = request.user
        if request.method:
            log_data['request_type'] = request.method
        if request.META:
            if 'HTTP_USER_AGENT' in request.META:
                log_data['user_agent'] = request.META['HTTP_USER_AGENT']
            if 'REMOTE_ADDR' in request.META:
                log_data['ip_address'] = request.META['REMOTE_ADDR']
        Audit.objects.create(**log_data)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

