# Generated by Django 4.2.1 on 2023-06-06 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0023_alter_land_tenurship_farmer_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='land_tenurship',
            old_name='titles',
            new_name='tenure_status',
        ),
        migrations.AddField(
            model_name='farm',
            name='farmer_ID',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='gcna_data.user_info', to_field='farmer_ID'),
        ),
        migrations.AddField(
            model_name='state',
            name='farmer_ID',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='gcna_data.user_info', to_field='farmer_ID'),
        ),
        migrations.AddField(
            model_name='symmary',
            name='farmer_ID',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='gcna_data.user_info', to_field='farmer_ID'),
        ),
        migrations.AddField(
            model_name='tree',
            name='farmer_ID',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='gcna_data.user_info', to_field='farmer_ID'),
        ),
    ]