from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

urlpatterns = i18n_patterns(
   path('', include('main.urls')),
   path('admin/', admin.site.urls),
)