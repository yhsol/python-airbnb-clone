from django.shortcuts import render, redirect
from . import models
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/all_rooms.html", {"page": rooms},)
    except EmptyPage:
        rooms = paginator.page(1)
        return redirect("/")
    except InvalidPage:
        rooms = paginator.page(1)
        return redirect("/")
    except Exception:
        rooms = paginator.page(1)
        return redirect("/")
    print(vars(rooms.paginator))
