from django.db import models
from django.db.models import SET
from django.utils.translation import gettext_lazy as _
from datetime import datetime


# Create your models here.
class Faction(models.Model):
    COVENANT = 'COV'
    MARAUDER = 'MAR'
    SYNDICATE = 'SYN'
    UNFACTIONED = 'UNF'
    FACTION_CHOICES = [(COVENANT, 'Covenant'),
                       (MARAUDER, 'Marauder'),
                       (SYNDICATE, 'Syndicate'),
                       (UNFACTIONED, 'No Faction')]
    faction = models.CharField(max_length=3, choices=FACTION_CHOICES, default=UNFACTIONED)


class Company(models.Model):
    company_id = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    faction = models.CharField(max_length=3, choices=Faction.FACTION_CHOICES, default=Faction.UNFACTIONED)

    def __str__(self):
        return f' id: {self.company_id}, company_name: {self.company_name}, faction: {self.faction} '