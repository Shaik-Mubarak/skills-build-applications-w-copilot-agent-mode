"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""

import os

from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

CODESPACE_NAME = os.environ.get("CODESPACE_NAME", "")
BASE_URL = f"https://{CODESPACE_NAME}-8000.app.github.dev"


def api_root(request):
    return JsonResponse({
        "message": "OctoFit Tracker API is running",
        "activities": f"{BASE_URL}/api/activities/",
    })


urlpatterns = [
    path('', api_root),
    path('admin/', admin.site.urls),
]curl http://127.0.0.1:8000