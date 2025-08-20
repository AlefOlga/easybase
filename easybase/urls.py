from movies.views import *

from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static
from easybase import settings  

urlpatterns = [
    path('', include('movies.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound