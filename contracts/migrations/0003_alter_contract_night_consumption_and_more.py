# Generated by Django 4.1.4 on 2022-12-27 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_alter_contract_night_consumption_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='night_consumption',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='night_consumption',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
