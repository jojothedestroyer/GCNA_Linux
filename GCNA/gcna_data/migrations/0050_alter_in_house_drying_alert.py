# Generated by Django 4.2.1 on 2023-07-07 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0049_cracking_summary_nutmeg_id_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='in_house_drying',
            name='ALERT',
            field=models.CharField(max_length=50, null=True, verbose_name='Alert'),
        ),
    ]
