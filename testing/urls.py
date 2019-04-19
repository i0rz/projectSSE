from django.urls import path
from . import views
from .models import LogMessage
from django.contrib import admin


home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:10],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="testing/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("about/",views.about, name="about"),
    path("contact/",views.contact, name="contact"),
    path("testing/<name>", views.hello_there, name="hello_there"),
    path("log/", views.log_message, name="log"),
    path("admin/", admin.site.urls),
    path('signup/', views.SignUp.as_view(), name='signup'),
    #first arg is a route "hello/" that accepts a variable string called name,
    #the string is passed to the views.hello_there
]

