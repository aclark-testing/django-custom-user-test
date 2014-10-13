from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'custom_user.custom_user.views.home', name='home'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    (r'^accounts/login/', 'custom_user.custom_user.views.signin'),

    (r'^logout/', 'custom_user.custom_user.views.signout'),
)
