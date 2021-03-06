# Generated by Django 3.2.9 on 2021-12-07 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nwcs', '0005_auto_20211206_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='player_pr_weapon_1',
            field=models.CharField(choices=[('SS', 'Sword & Shield'), ('RA', 'Rapier'), ('HA', 'Hatchet'), ('GA', 'Great Axe'), ('WH', 'War Hammer'), ('SP', 'Spear'), ('BW', 'Bow'), ('MU', 'Musket'), ('LS', 'Life Staff'), ('FS', 'Fire Staff'), ('IG', 'Ice Gauntlet'), ('VG', 'Void Gauntlet')], default='', max_length=255),
        ),
        migrations.AddField(
            model_name='player',
            name='player_pr_weapon_2',
            field=models.CharField(choices=[('SS', 'Sword & Shield'), ('RA', 'Rapier'), ('HA', 'Hatchet'), ('GA', 'Great Axe'), ('WH', 'War Hammer'), ('SP', 'Spear'), ('BW', 'Bow'), ('MU', 'Musket'), ('LS', 'Life Staff'), ('FS', 'Fire Staff'), ('IG', 'Ice Gauntlet'), ('VG', 'Void Gauntlet')], default='', max_length=255),
        ),
        migrations.AddField(
            model_name='player',
            name='player_sr_weapon_1',
            field=models.CharField(choices=[('SS', 'Sword & Shield'), ('RA', 'Rapier'), ('HA', 'Hatchet'), ('GA', 'Great Axe'), ('WH', 'War Hammer'), ('SP', 'Spear'), ('BW', 'Bow'), ('MU', 'Musket'), ('LS', 'Life Staff'), ('FS', 'Fire Staff'), ('IG', 'Ice Gauntlet'), ('VG', 'Void Gauntlet')], default='', max_length=255),
        ),
        migrations.AddField(
            model_name='player',
            name='player_sr_weapon_2',
            field=models.CharField(choices=[('SS', 'Sword & Shield'), ('RA', 'Rapier'), ('HA', 'Hatchet'), ('GA', 'Great Axe'), ('WH', 'War Hammer'), ('SP', 'Spear'), ('BW', 'Bow'), ('MU', 'Musket'), ('LS', 'Life Staff'), ('FS', 'Fire Staff'), ('IG', 'Ice Gauntlet'), ('VG', 'Void Gauntlet')], default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_company_id',
            field=models.ForeignKey(on_delete=models.SET(''), to='nwcs.company'),
        ),
    ]
