from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'deploydjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'deploydjango.views.home'),
    url(r'^home/$', 'deploydjango.views.home'),
    url(r'^deployapp/home/$', 'deployapp.views.home'),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, documment_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, documment_root=settings.MEDIA_ROOT)