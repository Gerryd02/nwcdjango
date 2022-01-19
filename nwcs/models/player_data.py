from django.db import models
from django.db.models import SET
from django.utils.translation import gettext_lazy as _
from datetime import datetime
import nwcs.models.company_data as c


class Player(models.Model):
    HEALER = 'Healer'
    TANK = 'Tank'
    SUPPORT = 'Support'
    RANGED = 'Ranged-DPS'
    MELEE = 'Melee-DPS'
    HYBRID = 'Hybrid'
    ROLES = [(HEALER, 'Healer'), (TANK, 'Tank'), (SUPPORT, 'Support'), (RANGED, 'Ranged-DPS'), (MELEE, 'Melee-DPS'),
             (HYBRID, 'Hybrid')]
    WEAPONS = [('Sword & Shield', 'Sword & Shield'), ('Rapier', 'Rapier'), ('Hatchet', 'Hatchet'),
               ('Great Axe', 'Great Axe'), ('War Hammer', 'War Hammer'), ('Spear', 'Spear'), ('Bow', 'Bow'),
               ('Musket', 'Musket'), ('Life Staff', 'Life Staff'),('Fire Staff', 'Fire Staff'),
               ('Ice Gauntlet', 'Ice Gauntlet'), ('Void Gauntlet', 'Void Gauntlet')]
    player_id = models.BigAutoField(primary_key=True)
    player_name = models.CharField(max_length=255, null=False, unique=True)
    player_level = models.IntegerField(null=False, default=1)
    player_company = models.ForeignKey(c.Company, on_delete=SET(""))
    player_faction = models.CharField(max_length=3, choices=c.Faction.FACTION_CHOICES, default=c.Faction.UNFACTIONED)
    player_primary_role = models.CharField(max_length=255, choices=ROLES, default="")
    player_pr_weapon_1 = models.CharField(max_length=255, choices=WEAPONS, default="")
    player_pr_weapon_2 = models.CharField(max_length=255, choices=WEAPONS, default="")
    player_secondary_role = models.CharField(max_length=255, choices=ROLES, default="")
    player_sr_weapon_1 = models.CharField(max_length=255, choices=WEAPONS, default="")
    player_sr_weapon_2 = models.CharField(max_length=255, choices=WEAPONS, default="")

    def __str__(self):
        return f'{self.player_name}'


class Expertise(models.Model):
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
    exp_player_name = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str([self.exp_sword, self.exp_shield, self.exp_rapier, self.exp_hatchet, self.exp_great_axe,
                    self.exp_war_hammer, self.exp_spear,
                    self.exp_bow, self.exp_musket, self.exp_life_staff, self.exp_fire_staff, self.exp_ice_gauntlet,
                    self.exp_void_gauntlet,
                    self.exp_head, self.exp_chest, self.exp_hands, self.exp_legs, self.exp_feet, self.exp_amulet,
                    self.exp_ring, self.exp_earring, self.exp_player_name, self.exp_player_name])


class Weapon(models.Model):
    level_sword = models.IntegerField(default=1)
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
    weapon_player_name = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)


class Gathering(models.Model):
    mining = models.IntegerField(default=0)
    harvesting = models.IntegerField(default=0)
    logging = models.IntegerField(default=0)
    skinning = models.IntegerField(default=0)
    fishing = models.IntegerField(default=0)
    gathering_player_name = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)


class Refining(models.Model):
    stone_cutting = models.IntegerField(default=0)
    smelting = models.IntegerField(default=0)
    weaving = models.IntegerField(default=0)
    woodworking = models.IntegerField(default=0)
    tanning = models.IntegerField(default=0)
    refining_player_name = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)


class Crafting(models.Model):
    arcana = models.IntegerField(default=0)
    armoring = models.IntegerField(default=0)
    cooking = models.IntegerField(default=0)
    engineering = models.IntegerField(default=0)
    furnishing = models.IntegerField(default=0)
    jewel_crafting = models.IntegerField(default=0)
    weapon_smithing = models.IntegerField(default=0)
    crafting_player_name = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)