from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
]

# only add this in when in debug mode
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
