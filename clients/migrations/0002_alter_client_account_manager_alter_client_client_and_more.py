# Generated by Django 4.1.4 on 2022-12-29 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_managers', '0001_initial'),
        ('client_managers', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='account_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_manager_clients', to='account_managers.accountmanager', verbose_name='Account Manager'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client',
            field=models.CharField(max_length=255, unique=True, verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_manager_clients', to='client_managers.clientmanager', verbose_name='Client Manager'),
        ),
        migrations.AlterField(
            model_name='historicalclient',
            name='account_manager',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='account_managers.accountmanager', verbose_name='Account Manager'),
        ),
        migrations.AlterField(
            model_name='historicalclient',
            name='client',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='historicalclient',
            name='client_manager',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='client_managers.clientmanager', verbose_name='Client Manager'),
        ),
    ]