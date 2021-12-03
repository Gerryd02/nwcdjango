from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class PlayerCard(View):

    def get(self, request, *args, **kwargs):
        return render(request, "player_card.html")


class Company(View):

    def get(self, request, *args, **kwargs):
        return render(request, "company_summary.html")


class Territories(View):

    def get(self, request, *args, **kwargs):
        return render(request, "territories.html")