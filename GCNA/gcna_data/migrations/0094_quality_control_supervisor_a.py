# Generated by Django 4.2.1 on 2023-09-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0093_rename_assortor_quality_control_assortor1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quality_control',
            name='SUPERVISOR_A',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
