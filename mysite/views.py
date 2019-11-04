from django.http import HttpResponseRedirect
from django.urls import reverse

def redirect_to_polls(request):
    # redirect user to the polls index
    return HttpResponseRedirect(reverse('polls:index'))