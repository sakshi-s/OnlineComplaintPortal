

from django.conf.urls import url
from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
]
