# Generated by Django 4.2.1 on 2023-05-23 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0008_alter_fullform_date_alter_fullform_inspected_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='crops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='fullform',
            name='other_crops',
        ),
        migrations.AddField(
            model_name='fullform',
            name='other_crops',
            field=models.ManyToManyField(to='gcna_data.crops'),
        ),
    ]
