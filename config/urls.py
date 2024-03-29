from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("fastbank/", include("fastbank.urls")),
    path(r"auth/", include("djoser.urls")),
    path(r"auth/", include("djoser.urls.jwt")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)