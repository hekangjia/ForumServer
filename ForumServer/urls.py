# coding=utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

userUrls = patterns('user_app.ajaxs',
    url(r'^login/', 'login', name="login"),
    url(r'^logout/', 'logout', name="logout"),
    url(r'^reg/', 'reg', name="reg"),
)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ForumServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', 'user_app.views.test'),
    url(r'^user/', include(userUrls)),
)
