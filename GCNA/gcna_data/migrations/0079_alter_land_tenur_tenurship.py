# Generated by Django 4.2.1 on 2023-08-21 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0078_citrus_mango_trees_parish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='land_tenur',
            name='tenurship',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
