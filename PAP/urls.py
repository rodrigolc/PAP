from django.conf.urls import patterns, include, url

from django.contrib import admin


admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PAP.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^usuarios/',include('usuarios.urls')),
    url(r'^pages/',include('pages.urls')),
    url(r'^widgets/',include('widgets.urls')),
)
