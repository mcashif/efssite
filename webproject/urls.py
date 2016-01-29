from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^efs/', include('efs.urls', namespace="efs")),
    url(r'^admin/logout/$', 'efs.views.logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logged_in/$', 'efs.views.logged_in'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'efs/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'efs/logout.html'}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)