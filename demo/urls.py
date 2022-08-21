from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from employee_list.views import *

urlpatterns = [
    path('', include('employee_list.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)