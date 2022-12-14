# Generated by Django 4.0.5 on 2022-11-02 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vaccines_control', '0004_alter_stockhistory_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='vaccine_name',
            field=models.CharField(blank=True, choices=[('BCG', 'BCG'), ('DPT-HepB-Hib', 'DPT-HepB-Hib'), ('OPV', 'OPV'), ('IPV', 'IPV'), ('Rotavirus vaccine', 'Rotavirus vaccine'), ('Yellow Fever', 'Yellow Fever'), ('Measles Rubella', 'Measles Rubella'), ('PCV', 'PCV'), ('HPV', 'HPV'), ('Tetanus Toxiod diptheria(Td)', 'Tetanus Toxiod diptheria(Td)')], max_length=50, null=True),
        ),
    ]
