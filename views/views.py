from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class Player(View):

    def get(self, request, *args, **kwargs):
        return render(request, "shared/player_data/../templates/shared/player.html")


class WeaponLevel(View):

    def get(self, request, *args, **kwargs):
        return render(request, "shared/player_data/../templates/shared/weapon_level.html")


class Crafting(View):

    def get(self, request, *args, **kwargs):
        return render(request, "shared/player_data/../templates/shared/crafting.html")


class Gathering(View):

    def get(self, request, *args, **kwargs):
        return render(request, "shared/player_data/../templates/shared/gathering.html")


class Refining(View):

    def get(self, request, *args, **kwargs):
        return render(request, "shared/player_data/../templates/shared/refining.html")

class PlayerCard(View):

    def get(self, request, *args, **kwargs):
        return render(request, "player_card.html")
