# Generated by Django 3.2.19 on 2023-05-14 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0007_employé_occupe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employé',
            name='nbr_taches',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employé',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employé',
            name='salair',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
