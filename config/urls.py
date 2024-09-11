from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('todo.urls')),
]

if settings.DEBUG:
    urlpatterns += [

    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
