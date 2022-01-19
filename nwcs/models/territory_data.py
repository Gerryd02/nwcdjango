from django.db import models
from django.db.models import SET
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from nwcs.models import company_data as c

class Territory(models.Model):
    BRIGHTWOOD = 'BW '
    CUTLASSKEYS = 'CK'
    EBONSCALE = 'ER'
    EVERFALL = 'EF'
    FIRSTLIGHT = 'FL'
    MONARCHS = 'MB'
    MOURNING = 'MD'
    REEK = "RW"
    RESTLESS = 'RS'
    WEAVERS = 'WF'
    WINDSWARD = 'WW'
    TERRITORY_CHOICES = [
        (BRIGHTWOOD, 'Brightwood'),
        (CUTLASSKEYS, 'Cutlass Keys'),
        (EBONSCALE, 'Ebonscale Reach'),
        (EVERFALL, 'Everfall'),
        (FIRSTLIGHT, 'First Light'),
        (MONARCHS, 'Monarchs Bluff'),
        (MOURNING, 'Mourningdale'),
        (REEK, 'Reekwater'),
        (RESTLESS, 'Restless Shores'),
        (WEAVERS, 'Weavers Fen'),
        (WINDSWARD, 'Windsward'),
    ]
    territory_name = models.CharField(max_length=255, choices=TERRITORY_CHOICES, unique=True, primary_key=True)
    controlling_company = models.ForeignKey(c.Company, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.territory_name}'


class Taxes(models.Model):
    tax_record_id = models.BigAutoField(primary_key=True)
    tax_territory = models.ForeignKey(Territory, on_delete=models.DO_NOTHING)
    housing_tax = models.FloatField(default=5.0)
    trading_tax = models.FloatField(default=3.0)
    refining_tax = models.FloatField(default=1.0)
    crafting_tax = models.FloatField(default=1.0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.housing_tax}, {self.trading_tax}, {self.refining_tax}, {self.crafting_tax}'


class Income(models.Model):
    income_record_id = models.BigAutoField(primary_key=True)
    income_territory = models.ForeignKey(Territory, on_delete=models.DO_NOTHING)
    housing_income = models.FloatField(default=0.0)
    trading_income = models.FloatField(default=0.0)
    refining_income = models.FloatField(default=0.0)
    crafting_income = models.FloatField(default=0.0)
    total_income = models.Aggregate(housing_income, trading_income, refining_income, crafting_income)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.housing_income}, {self.trading_income}, {self.refining_income}, {self.crafting_income}'


class CraftingTier(models.Model):
    TIER_1 = 'T1'
    TIER_2 = 'T2'
    TIER_3 = 'T3'
    TIER_4 = 'T4'
    TIER_5 = 'T5'

    TIER_CHOICES = [
        (TIER_1, 'tier_1'),
        (TIER_2, 'tier_2'),
        (TIER_3, 'tier_3'),
        (TIER_4, 'tier_4'),
        (TIER_5, 'tier_5'),
    ]

    tiers = models.CharField(max_length=2, choices=TIER_CHOICES, default=TIER_1)


class SettlementUpgrades(models.Model):
    settlement_upgrade_id = models.BigAutoField(primary_key=True, default='1')
    loom = models.CharField(max_length=2, choices=CraftingTier.TIER_CHOICES, default=CraftingTier.TIER_1)
    smelter = models.CharField(max_length=2, choices=CraftingTier.TIER_CHOICES, default=CraftingTier.TIER_1)
    stone_cutting_table = models.CharField(max_length=2, choices=CraftingTier.TIER_CHOICES, default=CraftingTier.TIER_1)
    tannery = models.CharField(max_length=2, choices=CraftingTier.TIER_CHOICES, default=CraftingTier.TIER_1)
    woodshop = models.CharField(max_length=2, choices=CraftingTier.TIER_CHOICES, default=CraftingTier.TIER_1)
    arcane_repository = models.CharField(max_length=2, choices=CraftingTier.TIER_CHOICES, default=CraftingTier.TIER_1)
    forge = models.CharField(max_length=2, choices=CraftingTier.TIER_CHOICES, default=CraftingTier.TIER_1)
    kitchen = models.CharField(max_length=2, choices=CraftingTier.TIER_CHOICES, default=CraftingTier.TIER_1)
    outfitters = models.CharField(max_length=2, choices=CraftingTier.TIER_CHOICES, default=CraftingTier.TIER_1)
    workshop = models.CharField(max_length=2, choices=CraftingTier.TIER_CHOICES, default=CraftingTier.TIER_1)
    current_territory = models.ForeignKey(Territory, on_delete=models.DO_NOTHING, default="")
    last_updated = models.DateTimeField(auto_now=True)


class FortUpgrades(models.Model):
    fort_upgrade_id = models.BigAutoField(primary_key=True)
    ballista = models.CharField(max_length=2, choices=CraftingTier.TIER_CHOICES, default=CraftingTier.TIER_1)
    burning_oil_vat = models.CharField(max_length=2, choices=CraftingTier.TIER_CHOICES, default=CraftingTier.TIER_1)
    emplacement_points = models.CharField(max_length=2, choices=CraftingTier.TIER_CHOICES, default=CraftingTier.TIER_1)
    explosives = models.CharField(max_length=2, choices=CraftingTier.TIER_CHOICES, default=CraftingTier.TIER_1)
    gates = models.CharField(max_length=2, choices=CraftingTier.TIER_CHOICES, default=CraftingTier.TIER_1)
    repeaters = models.CharField(max_length=2, choices=CraftingTier.TIER_CHOICES, default=CraftingTier.TIER_1)
    warhorns = models.CharField(max_length=2, choices=CraftingTier.TIER_CHOICES, default=CraftingTier.TIER_1)
    current_territory = models.ForeignKey(Territory, on_delete=models.DO_NOTHING, default="")
    last_updated = models.DateTimeField(auto_now=True)