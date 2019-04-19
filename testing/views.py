from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LogMessageForm
from .models import LogMessage
from django.views.generic import ListView
import re

from datetime import datetime
# Create your views here.
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "testing/about.html")

def contact(request):
    return render(request, "testing/contact.html")

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "testing/log_message.html", {"form": form})


def hello_there(request, name):
    return render(
        request,
        'testing/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
    # now = datetime.now()
    # formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # # Filter the name argument to letters only using regular expressions. URL arguments
    # # can contain arbitrary text, so we restrict to safe characters only.
    # match_object = re.match("[a-zA-Z]+", name)

    # if match_object:
    #     clean_name = match_object.group(0)
    # else:
    #     clean_name = "Friend"

    # # content = "Hello there, " + clean_name + "! It's " + formatted_now
    # content = "<h1>Hello there, " + clean_name + "! It's "+formatted_now+"</h1>"
    # return HttpResponse(content)
