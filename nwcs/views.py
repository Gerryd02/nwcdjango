from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import nwcs.models as m


# Create your views here.


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class PlayerCard(View):
    expertise = m.Expertise.objects.filter(exp_player_name_id=1)
    context = {'exp': expertise}
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
