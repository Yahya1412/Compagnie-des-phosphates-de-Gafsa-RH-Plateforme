# Generated by Django 3.2.19 on 2023-05-12 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0006_auto_20230511_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='employé',
            name='occupe',
            field=models.BooleanField(default=False),
        ),
    ]
