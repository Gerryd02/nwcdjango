from django import forms
from nwcs.models.company_data import Company
from nwcs.models.player_data import Player, Weapon, Expertise, Gathering, Crafting, Refining
from nwcs.models.territory_data import Territory, Taxes, SettlementUpgrades, FortUpgrades, CraftingTier, Income
from django.forms import ModelForm


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['player_name', 'player_level', 'player_faction', 'player_company', 'player_primary_role',
                  'player_secondary_role', 'player_pr_weapon_1', 'player_pr_weapon_2', 'player_sr_weapon_1',
                  'player_sr_weapon_2']


class ExpertiseForm(ModelForm):
    class Meta:
        model = Expertise
        fields = ['exp_sword', 'exp_shield', ]
