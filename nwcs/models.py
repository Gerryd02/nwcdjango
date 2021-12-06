from django.db import models
from django.db.models import SET
from django.utils.translation import gettext_lazy as _
from datetime import datetime


# Create your models here.
class Factions(models.Model):
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
    faction = Factions.FACTION_CHOICES

    def __str__(self):
        return f' id: {self.company_id}, company_name: {self.company_name}, faction: {self.faction} '


class Player(models.Model):
    player_id = models.BigAutoField(primary_key=True)
    player_name = models.CharField(max_length=255, null=False)
    player_level = models.IntegerField(null=False, default=1)
    player_company_id = models.ForeignKey(Company, on_delete=SET(4))
    player_faction = Factions.FACTION_CHOICES

    def __str__(self):
        return f' id: {self.player_id}, player_name: {self.player_name}, player_level {self.player_level}, ' \
               f'company_id: {self.player_company_id}, player_faction: {self.player_faction} '


class Expertise(Player):
    exp_sword = models.IntegerField(default=500)
    exp_shield = models.IntegerField(default=500)
    exp_rapier = models.IntegerField(default=500)
    exp_hatchet = models.IntegerField(default=500)
    exp_great_axe = models.IntegerField(default=500)
    exp_war_hammer = models.IntegerField(default=500)
    exp_spear = models.IntegerField(default=500)
    exp_bow = models.IntegerField(default=500)
    exp_musket = models.IntegerField(default=500)
    exp_life_staff = models.IntegerField(default=500)
    exp_fire_staff = models.IntegerField(default=500)
    exp_ice_gauntlet = models.IntegerField(default=500)
    exp_void_gauntlet = models.IntegerField(default=500)
    exp_head = models.IntegerField(default=500)
    exp_chest = models.IntegerField(default=500)
    exp_hands = models.IntegerField(default=500)
    exp_legs = models.IntegerField(default=500)
    exp_feet = models.IntegerField(default=500)
    exp_amulet = models.IntegerField(default=500)
    exp_ring = models.IntegerField(default=500)
    exp_earring = models.IntegerField(default=500)

    def __str__(self):
        return f' {[self.field for i in Expertise.field_names]}'


class Weapon(Player):
    level_sword = models.IntegerField(default=1)
    level_shield = models.IntegerField(default=1)
    level_rapier = models.IntegerField(default=1)
    level_hatchet = models.IntegerField(default=1)
    level_great_axe = models.IntegerField(default=1)
    level_war_hammer = models.IntegerField(default=1)
    level_spear = models.IntegerField(default=1)
    level_bow = models.IntegerField(default=1)
    level_musket = models.IntegerField(default=1)
    level_life_staff = models.IntegerField(default=1)
    level_fire_staff = models.IntegerField(default=1)
    level_ice_gauntlet = models.IntegerField(default=1)
    level_void_gauntlet = models.IntegerField(default=1)

    def __str__(self):
        return f' {[self.field for i in Weapon.field_names]}'


class Gathering(Player):
    mining = models.IntegerField(default=0)
    harvesting = models.IntegerField(default=0)
    logging = models.IntegerField(default=0)
    skinning = models.IntegerField(default=0)
    fishing = models.IntegerField(default=0)

    def __str__(self):
        return f' {[self.field for i in Gathering.field_names]}'


class Refining(Player):
    stone_cutting = models.IntegerField(default=0)
    smelting = models.IntegerField(default=0)
    weaving = models.IntegerField(default=0)
    woodworking = models.IntegerField(default=0)
    cooking = models.IntegerField(default=0)
    tannning = models.IntegerField(default=0)

    def __str__(self):
        return f' {[self.field for i in Refining.field_names]}'


class Crafting(Player):
    arcana = models.IntegerField(default=0)
    armoring = models.IntegerField(default=0)
    cooking = models.IntegerField(default=0)
    engineering = models.IntegerField(default=0)
    furnishing = models.IntegerField(default=0)
    jewel_crafting = models.IntegerField(default=0)
    weapon_smithing = models.IntegerField(default=0)

    def __str__(self):
        return f' {[self.field for i in Crafting.field_names]}'


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
    territory_name = models.CharField(max_length=255, choices=TERRITORY_CHOICES, unique=True)
    controlling_company = Factions.FACTION_CHOICES

    def __str__(self):
        return f' territory: {self.territory_name}, company: {self.controlling_company}'


class Taxes(Territory):
    housing_tax = models.FloatField(default=5.0)
    trading_tax = models.FloatField(default=3.0)
    refining_tax = models.FloatField(default=1.0)
    crafting_tax = models.FloatField(default=1.0)
    controlling_company = Territory.controlling_company
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.housing_tax}, {self.trading_tax}, {self.refining_tax}, {self.crafting_tax}, ' \
               f'{self.controlling_company}'


class Income(Territory):
    housing_income = models.FloatField(default=0.0)
    trading_income = models.FloatField(default=0.0)
    refining_income = models.FloatField(default=0.0)
    crafting_income = models.FloatField(default=0.0)
    total_income = models.Aggregate(housing_income, trading_income, refining_income, crafting_income)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.housing_income}, {self.trading_income}, {self.refining_income}, {self.crafting_income}, ' \
               f'{self.controlling_company} '


class CraftingTiers(models.Model):
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


class SettlementUpgrades(Territory):

    loom = CraftingTiers.tiers
    smelter = CraftingTiers.tiers
    stone_cutting_table = CraftingTiers.tiers
    tannery = CraftingTiers.tiers
    woodshop = CraftingTiers.tiers
    arcane_repository = CraftingTiers.tiers
    forge = CraftingTiers.tiers
    kitchen = CraftingTiers.tiers
    outfitters = CraftingTiers.tiers
    workshop = CraftingTiers.tiers
    last_updated = models.DateTimeField(auto_now=True)


class FortUpgrades(Territory):

    ballista = CraftingTiers.tiers
    burning_oil_vat = CraftingTiers.tiers
    emplacement_points = CraftingTiers.tiers
    explosives = CraftingTiers.tiers
    gates = CraftingTiers.tiers
    repeaters = CraftingTiers.tiers
    warhorns = CraftingTiers.tiers
    last_updated = models.DateTimeField(auto_now=True)

