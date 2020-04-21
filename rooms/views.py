from math import ceil
from django.shortcuts import render
from . import models
from django.core.paginator import Paginator


def all_rooms(request):
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)
    print(vars(rooms.paginator))
    return render(request, "rooms/all_rooms.html", {"rooms": rooms},)
