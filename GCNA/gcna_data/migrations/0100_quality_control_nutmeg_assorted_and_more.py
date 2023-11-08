# Generated by Django 4.2.1 on 2023-09-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0099_alter_in_house_drying_alert_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quality_control',
            name='Nutmeg_Assorted',
            field=models.CharField(choices=[('', 'Select'), ('Sounds', 'Sounds'), ('Lights', 'Lights'), ("110's", "110's"), ('Other', 'Other')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quality_control',
            name='REWORK',
            field=models.CharField(choices=[('', 'Select'), ('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True),
        ),
    ]