# Generated by Django 4.2.1 on 2023-09-13 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0091_rename_signed_by_floated_moisture_analysis_a_approved_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='floated_moisture_analysis_b',
            name='Total_Weight_H',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='floated_moisture_analysis_b',
            name='Total_Weight_L',
            field=models.FloatField(default=0),
        ),
    ]
