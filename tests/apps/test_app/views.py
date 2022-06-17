from django.http import HttpResponse
from tests.apps.test_app.models import TestModel


def create_sample_view(request):
    sample = TestModel.objects.create()
    return HttpResponse(sample)
