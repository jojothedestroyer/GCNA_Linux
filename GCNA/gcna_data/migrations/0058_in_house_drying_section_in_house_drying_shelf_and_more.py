# Generated by Django 4.2.1 on 2023-07-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0057_rename_section_ground_1_in_house_drying_sectiong_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='in_house_drying',
            name='Section',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='Shelf',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='Tray',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ALERT',
            field=models.CharField(blank=True, choices=[('', '--Send Alert?--'), ('Y', 'Yes'), ('N', 'No')], max_length=50, null=True, verbose_name='Alert'),
        ),
    ]
