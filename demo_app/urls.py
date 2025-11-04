from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome! Django demo app is running 🎉</h1><p>Visit /api/ for API endpoints.</p>")

urlpatterns = [
    path("", home),  # 👈 add this line
    path("admin/", admin.site.urls),
    path("api/", include("core.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
