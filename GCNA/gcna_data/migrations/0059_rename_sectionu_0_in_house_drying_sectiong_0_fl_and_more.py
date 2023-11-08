# Generated by Django 4.2.1 on 2023-07-24 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0058_in_house_drying_section_in_house_drying_shelf_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='SectionU_0',
            new_name='SectionG_0_FL',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='SectionGP',
            new_name='SectionG_0_GF',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='SectionGP_0',
            new_name='SectionG_1F',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='SectionG_0',
            new_name='SectionG_2F',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='SectionH',
            new_name='SectionG_FL',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='SectionH_0',
            new_name='SectionG_GF',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='SectionM_0',
            new_name='SectionH_0_1F',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='SectionU',
            new_name='SectionH_0_2F',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='ShelfGP',
            new_name='ShelfGP_0_1F',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='ShelfGP_0',
            new_name='ShelfGP_0_2F',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='ShelfG_0',
            new_name='ShelfGP_0_FL',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='ShelfH',
            new_name='ShelfGP_0_GF',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='ShelfH_0',
            new_name='ShelfGP_1F',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='ShelfM',
            new_name='ShelfGP_2F',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='ShelfM_0',
            new_name='ShelfGP_FL',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='ShelfU',
            new_name='ShelfGP_GF',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='ShelfU_0',
            new_name='ShelfG_0_1F',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='TrayGP',
            new_name='TrayGP_0_1F',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='TrayGP_0',
            new_name='TrayGP_0_2F',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='TrayG_0',
            new_name='TrayGP_0_FL',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='TrayH_0',
            new_name='TrayGP_0_GF',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='TrayH',
            new_name='TrayGP_1F',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='TrayM',
            new_name='TrayGP_2F',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='TrayM_0',
            new_name='TrayGP_FL',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='TrayU',
            new_name='TrayGP_GF',
        ),
        migrations.RenameField(
            model_name='in_house_drying',
            old_name='TrayU_0',
            new_name='TrayG_0_1F',
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionGP_0_1F',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionGP_0_2F',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionGP_0_FL',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionGP_0_GF',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionGP_1F',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionGP_2F',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionGP_FL',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionGP_GF',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionG_0_1F',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionG_0_2F',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionH_0_FL',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionH_0_GF',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionH_1F',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionH_2F',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionH_FL',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionH_GF',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionM_0_1F',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionM_0_2F',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionM_0_FL',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionM_0_GF',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionM_1F',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionM_2F',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionM_FL',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionM_GF',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionU_0_1F',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionU_0_2F',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionU_0_FL',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionU_0_GF',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionU_1F',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionU_2F',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionU_FL',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='SectionU_GF',
            field=models.CharField(choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfG_0_2F',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfG_0_FL',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfG_0_GF',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfG_1F',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfG_2F',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfG_FL',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfG_GF',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfH_0_1F',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfH_0_2F',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfH_0_FL',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfH_0_GF',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfH_1F',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfH_2F',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfH_FL',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfH_GF',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfM_0_1F',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfM_0_2F',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfM_0_FL',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfM_0_GF',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfM_1F',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfM_2F',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfM_FL',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfM_GF',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfU_0_1F',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfU_0_2F',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfU_0_FL',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfU_0_GF',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfU_1F',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfU_2F',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfU_FL',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='ShelfU_GF',
            field=models.CharField(choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayG_0_2F',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayG_0_FL',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayG_0_GF',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayG_1F',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayG_2F',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayG_FL',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayG_GF',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayH_0_1F',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayH_0_2F',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayH_0_FL',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayH_0_GF',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayH_1F',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayH_2F',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayH_FL',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayH_GF',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayM_0_1F',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayM_0_2F',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayM_0_FL',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayM_0_GF',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayM_1F',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayM_2F',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayM_FL',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayM_GF',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayU_0_1F',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayU_0_2F',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayU_0_FL',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayU_0_GF',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayU_1F',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayU_2F',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayU_FL',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AddField(
            model_name='in_house_drying',
            name='TrayU_GF',
            field=models.CharField(choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ALERT',
            field=models.CharField(blank=True, choices=[('', 'Send Alert?'), ('Y', 'Yes'), ('N', 'No')], max_length=50, null=True, verbose_name='Alert'),
        ),
    ]