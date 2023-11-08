# Generated by Django 4.2.1 on 2023-06-09 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0028_citrus_mango_trees_coconut_trees_condition_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='inspector_symmary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimated_annual_production', models.CharField(max_length=50, null=True)),
                ('estimated_peak_productions', models.CharField(max_length=50, null=True)),
                ('inspected_by', models.DateField(null=True, verbose_name='Inspection Date')),
                ('date', models.DateField(null=True, verbose_name='Current Date')),
            ],
        ),
        migrations.RemoveField(
            model_name='symmary',
            name='estimated_annual_production',
        ),
        migrations.RemoveField(
            model_name='symmary',
            name='estimated_peak_productions',
        ),
        migrations.AddField(
            model_name='symmary',
            name='annual_production',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='symmary',
            name='farmer_ID',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='gcna_data.user_info', to_field='farmer_ID'),
        ),
        migrations.AddField(
            model_name='symmary',
            name='peak_productions',
            field=models.CharField(max_length=50, null=True),
        ),
    ]