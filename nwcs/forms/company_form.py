from django import forms
from nwcs.models.company_data import Company
from nwcs.models.territory_data import Territory, Taxes, SettlementUpgrades, FortUpgrades, CraftingTier, Income
from django.forms import ModelForm


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'faction']
