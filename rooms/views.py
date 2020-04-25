from django.views.generic import ListView
from django.shortcuts import render
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    context_object_name = "rooms"


def room_detail(request, pk):

    return render(request, "rooms/detail.html")
