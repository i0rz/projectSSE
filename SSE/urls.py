from django.contrib import admin
from django.urls import include,path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView # new

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    path("", include("testing.urls")),
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += staticfiles_urlpatterns()

#Access login page here: http://localhost:8000/accounts/login/
