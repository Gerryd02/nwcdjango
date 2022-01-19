from django.contrib import admin
from nwcs.models import company_data as c, player_data as p, territory_data as t
# Register your models here.

admin.site.register(c.Company)
admin.site.register(p.Player)
admin.site.register(p.Expertise)
admin.site.register(p.Weapon)
admin.site.register(p.Gathering)
admin.site.register(p.Refining)
admin.site.register(p.Crafting)
admin.site.register(t.SettlementUpgrades)
admin.site.register(t.FortUpgrades)
admin.site.register(t.Taxes)
admin.site.register(t.Income)
admin.site.register(t.Territory)
