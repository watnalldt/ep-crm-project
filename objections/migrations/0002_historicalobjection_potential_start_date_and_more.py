# Generated by Django 4.1.4 on 2023-01-06 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalobjection',
            name='potential_start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Objection Date'),
        ),
        migrations.AddField(
            model_name='objection',
            name='potential_start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Objection Date'),
        ),
    ]
