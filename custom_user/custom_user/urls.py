from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'custom_user.custom_user.views.home', name='home'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    (r'^accounts/login/', 'custom_user.custom_user.views.signin'),

    (r'^logout/', 'custom_user.custom_user.views.signout'),

    (r'^password_change_form/', 'django.contrib.auth.views.password_change'),
    url(r'^password_change_done/', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
)
