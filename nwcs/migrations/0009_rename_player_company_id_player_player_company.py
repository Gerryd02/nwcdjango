# Generated by Django 4.0 on 2021-12-16 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nwcs', '0008_auto_20211207_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='player_company_id',
            new_name='player_company',
        ),
    ]
