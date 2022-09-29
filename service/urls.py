from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    re_path('media/files/?', include('media_service.urls'))

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)