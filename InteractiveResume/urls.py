"""
Definition of urls for InteractiveResume.
"""

from datetime import datetime
from django.conf.urls import patterns, url, include
from app.forms import BootstrapAuthenticationForm
from django.conf import settings
# Uncomment the next lines to enable the admin:
from django.contrib import admin

from django.conf.urls.static import static
from app.models import Application

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^history', 'app.views.history', name='history'),
    url(r'^education', 'app.views.education', name='education'),
    url(r'^workhistory/(?P<id>[\d]+)-(?P<slug>[-\w]+)/', 'app.views.workhistory', name='workhistory'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
                'current_application': Application.objects.get(pk=1),

            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),
    # url(r'^api-auth/', include("rest_framework.urls", namespace='rest_framework')),
    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
