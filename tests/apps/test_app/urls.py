from django.urls import re_path
from tests.apps.test_app import views

app_name = "test_app"

urlpatterns = [
    re_path("create-sample", views.create_sample_view, name="create-sample"),
]
