from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import nwcs.models as m


# Create your views here.


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class PlayerCard(View):
    expertise = m.Expertise.objects.get(exp_player_name='1')
    gathering = m.Gathering.objects.get(gathering_player_name='1')
    refining = m.Refining.objects.get(refining_player_name='1')
    crafting = m.Crafting.objects.get(crafting_player_name='1')
    weapons = m.Weapon.objects.get(weapon_player_name='1')
    context = {'exp': expertise, 'g': gathering, 'r': refining, 'c': crafting, 'w': weapons}

    def get(self, request, *args, **kwargs):
        return render(request, "player_card.html", context=self.context)


class Company(View):
    company_roster = m.Player.objects.filter(player_company_id_id=1)
    context = {'roster': company_roster}

    def get(self, request, *args, **kwargs):
        return render(request, "company_summary.html", context=self.context)


class Territories(View):

    def get(self, request, *args, **kwargs):
        return render(request, "territories.html")
