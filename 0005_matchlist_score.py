# Generated by Django 5.1.1 on 2024-10-05 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_playerslist_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchlist',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
