# Generated by Django 4.2.1 on 2023-08-21 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0080_land_tenur_training_land_tenur_visit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='land_tenur',
            name='farm_type',
            field=models.CharField(choices=[('', '--Select an option--'), ('Nutmeg', 'Nutmeg'), ('Coconut', 'Coconut')], default='P', max_length=100),
        ),
    ]