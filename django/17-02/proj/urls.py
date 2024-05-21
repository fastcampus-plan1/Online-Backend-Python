from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("product.urls")),
    # django.contrib.auth 모듈에 내장된 인증 URL
    path("accounts/", include("django.contrib.auth.urls")),
]
