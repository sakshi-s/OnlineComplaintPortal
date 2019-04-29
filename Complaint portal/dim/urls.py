
from django.conf.urls import url
from django.contrib import admin
from django.urls import include , path

urlpatterns = [
    url('admin/', admin.site.urls),
    path('', include('portal.urls')),
]
