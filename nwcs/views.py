from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import nwcs.models.player_data as p
import nwcs.models.territory_data as t
import nwcs.models.company_data as c
from nwcs.forms.player_forms import PlayerForm, ExpertiseForm


# Create your views here.

class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class PlayerCard(View):
    expertise = p.Expertise.objects
    gathering = p.Gathering.objects.get(gathering_player_name='1')
    refining = p.Refining.objects.get(refining_player_name='1')
    crafting = p.Crafting.objects.get(crafting_player_name='1')
    weapons = p.Weapon.objects.get(weapon_player_name='1')
    context = {'exp': expertise, 'g': gathering, 'r': refining, 'c': crafting, 'w': weapons}

    def get(self, request, *args, **kwargs):
        return render(request, "player_card.html", context=self.context)


class Company(View):
    company_roster = p.Player.objects.filter(player_company_id=1)
    context = {'roster': company_roster}

    def get(self, request, *args, **kwargs):
        return render(request, "company_summary.html", context=self.context)


class Territories(View):
    territory_list = t.Territory.objects
    taxes = t.Territory.objects.all()

    def get(self, request, *args, **kwargs):
        return render(request, "territories.html")


def get_player_info(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
        else:
            form = PlayerForm()
        return render(request, 'player_info.html', {'form': form})


def get_player_form(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = PlayerForm
    return render(request, 'form_templates/player_templates/player.html', {'form': form})
