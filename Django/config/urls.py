from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns

if 'survey' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^survey/', include('survey.urls'))
    ]
