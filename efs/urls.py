from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()generatefinal

urlpatterns = [
    # index page
    url(r'^$', 'efs.views.login', name='login'),
    url(r'^index/$', 'efs.views.index', name='index'),
    url(r'^sindhi/$', 'efs.views.sindhi', name='sindhi'),
    url(r'^urdu/$', 'efs.views.urdu', name='urdu'),
    url(r'^math/$', 'efs.views.math', name='math'),
    url(r'^english/$', 'efs.views.english', name='english'),
    url(r'^outcomes/(?P<subject>[0-9]+)/(?P<grader>[0-9]+)/$', 'efs.views.outcomelist', name='outcomelist'),
    url(r'^generate/(?P<subject>[0-9]+)/(?P<grader>[0-9]+)/(?P<ptype>[0-9]+)/$', 'efs.views.generatepaper', name='generatepaper'),
    url(r'^generatedanswer/$', 'efs.views.generateanswers', name='generateanswers'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)