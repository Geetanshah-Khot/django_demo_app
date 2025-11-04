from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import re_path

def home(request):
    return HttpResponse("<h1>Welcome! Django demo app is running 🎉</h1><p>Visit /api/ for API endpoints.</p>")

urlpatterns = [
    path("", home),  # homepage route
    path("admin/", admin.site.urls),
    path("api/", include("core.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^favicon\.ico$', serve, {'path': 'favicon.ico', 'document_root': settings.STATIC_ROOT}),
    ]
