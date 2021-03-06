# Generated by Django 3.2.9 on 2021-12-07 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nwcs', '0002_auto_20211206_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='player_primary_role',
            field=models.CharField(choices=[(1, 'Healer'), (2, 'Tank'), (3, 'Support'), (4, 'Ranged-DPS'), (5, 'Melee-DPS'), (6, 'Hybrid')], default='', max_length=255),
        ),
        migrations.AddField(
            model_name='player',
            name='player_secondary_role',
            field=models.CharField(choices=[(1, 'Healer'), (2, 'Tank'), (3, 'Support'), (4, 'Ranged-DPS'), (5, 'Melee-DPS'), (6, 'Hybrid')], default='', max_length=255),
        ),
    ]
