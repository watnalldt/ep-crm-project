# Generated by Django 4.1.4 on 2022-12-29 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0006_alter_contract_account_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='annualised_budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Annualised Budget'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='commission_per_annum',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Commission Per Annum'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='commission_per_contract',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Commission Per Contract'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='commission_per_unit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Commission Per Unit'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Contract Value'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='day_kilowatt_hour_rate',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Day Kilowatt Hour Rate'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='feed_in_tariff',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Feed In Tariff'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='future_contract_start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Future Contract Start Date'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='future_unit_rate_1',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Future Unit Rate 1'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='future_unit_rate_2',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Future Unit Rate 2'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='future_unit_rate_3',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Future Unit Rate 3'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='is_ooc',
            field=models.BooleanField(default=False, verbose_name='Out Of Contract'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='kva',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='KVA'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='night_rate',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=8, null=True, verbose_name='Night Rate'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='partner_commission',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Partner Commission'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='pence_per_kilowatt',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Pence Per Kilowatt'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='profile',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Profile'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='sc_frequency',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Standing Charge Frequency'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='seamless_status',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Seamless Status'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='smart_meter',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Smart Meter'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='standing_charge',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Standing Charge'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='unit_rate_1',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Unit Rate 1'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='unit_rate_2',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Unit Rate 2'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='unit_rate_3',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Unit Rate 3'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='annualised_budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Annualised Budget'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='commission_per_annum',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Commission Per Annum'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='commission_per_contract',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Commission Per Contract'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='commission_per_unit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Commission Per Unit'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='contract_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Contract Value'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='day_kilowatt_hour_rate',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Day Kilowatt Hour Rate'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='feed_in_tariff',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Feed In Tariff'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='future_contract_start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Future Contract Start Date'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='future_unit_rate_1',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Future Unit Rate 1'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='future_unit_rate_2',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Future Unit Rate 2'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='future_unit_rate_3',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Future Unit Rate 3'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='is_ooc',
            field=models.BooleanField(default=False, verbose_name='Out Of Contract'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='kva',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='KVA'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='night_rate',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=8, null=True, verbose_name='Night Rate'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='partner_commission',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Partner Commission'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='pence_per_kilowatt',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Pence Per Kilowatt'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='profile',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Profile'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='sc_frequency',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Standing Charge Frequency'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='seamless_status',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Seamless Status'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='smart_meter',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Smart Meter'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='standing_charge',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Standing Charge'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='unit_rate_1',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Unit Rate 1'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='unit_rate_2',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Unit Rate 2'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='unit_rate_3',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Unit Rate 3'),
        ),
    ]
