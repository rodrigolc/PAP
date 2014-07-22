from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'PAP.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^usuarios/', include('usuarios.urls')),
                       url(r'^widgets/', include('widgets.urls')),
                       url(r'^', include('pages.urls')),
                       ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
