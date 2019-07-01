from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
import blogweb.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include(blogweb.urls))
]