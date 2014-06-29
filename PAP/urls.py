from django.conf.urls import patterns, include, url

from django.contrib import admin
import page

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PAP.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^/','page.views.index'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^(?P<path>.*)','page.views.view_template'),
)
