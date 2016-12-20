from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'students.views.homepage', name='homepage'),
    url(r'student/', include('students.urls')),
    url(r'^media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT})
]
