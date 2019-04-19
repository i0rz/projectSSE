from django.contrib import admin
from django.urls import include,path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    path("", include("testing.urls")),
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += staticfiles_urlpatterns()
