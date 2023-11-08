# Generated by Django 4.2.1 on 2023-06-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0031_remove_farmer_info_photo_remove_land_info_farmer_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutmeg_frequency',
            name='Never',
        ),
        migrations.RemoveField(
            model_name='nutmeg_frequency',
            name='Occasional',
        ),
        migrations.RemoveField(
            model_name='nutmeg_frequency',
            name='Regular',
        ),
        migrations.RemoveField(
            model_name='nutmeg_land',
            name='Abandoned',
        ),
        migrations.RemoveField(
            model_name='nutmeg_land',
            name='Seasonal',
        ),
        migrations.RemoveField(
            model_name='nutmeg_land',
            name='norm_land',
        ),
        migrations.AddField(
            model_name='nutmeg_frequency',
            name='Frequency',
            field=models.CharField(choices=[('', 'Select'), ('Regular', 'Regular'), ('Occasional', 'Occasional'), ('Never', 'Never')], default='P', max_length=100, verbose_name='Select the frequency that best corresponds with the farm.'),
        ),
        migrations.AddField(
            model_name='nutmeg_land',
            name='farm_type',
            field=models.CharField(choices=[('', 'Select'), ('Normal', 'Normal'), ('Seasonal', 'Seasonal'), ('Abandoned', 'Abandoned')], default='P', max_length=100, verbose_name='Select the land type that best corresponds with the farm.'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='Drains',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Good'), ('N', 'Fair'), ('N', 'Poor')], default='P', max_length=1, verbose_name='What is the state of the drains Drains'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='Fertilizing',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Good'), ('N', 'Fair'), ('N', 'Poor')], default='P', max_length=1, verbose_name='What is the state of the Fertilizing'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='Harvesting',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Good'), ('N', 'Fair'), ('N', 'Poor')], default='P', max_length=1, verbose_name='What is the state of the Harvesting'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='Land_Clearing',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Good'), ('N', 'Fair'), ('N', 'Poor')], default='P', max_length=1, verbose_name='What is the state of the Land_Clearing'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='Planting',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Good'), ('N', 'Fair'), ('N', 'Poor')], default='P', max_length=1, verbose_name='What is the state of the Planting'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='Presence_of_pest_and_diseases_on_nutmegs',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Good'), ('N', 'Fair'), ('N', 'Poor')], default='P', max_length=1, verbose_name='What is the state of pests and diseases?'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='Presence_of_pest_and_diseases_on_nutmegs_cont',
            field=models.CharField(max_length=50, null=True, verbose_name='Elaborate the pest and dieseases present,if any.'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='Pruning',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Good'), ('N', 'Fair'), ('N', 'Poor')], default='P', max_length=1, verbose_name='What is the state of the Pruning'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='Weeds',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Good'), ('N', 'Fair'), ('N', 'Poor')], default='P', max_length=1, verbose_name='What is the state of the weeds? Weeds'),
        ),
        migrations.AlterField(
            model_name='farm_house',
            name='Farm_House',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Yes'), ('N', 'No')], default='P', max_length=1, verbose_name='Is a Farm house present'),
        ),
        migrations.AlterField(
            model_name='farm_water_source',
            name='is_water_treated',
            field=models.CharField(choices=[('', 'Was this water source is used?'), ('Y', 'Yes'), ('N', 'No')], default='P', max_length=1, verbose_name='Is the water source treated'),
        ),
        migrations.AlterField(
            model_name='farm_water_source',
            name='is_water_treated_cont',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='If the water was treated. How?'),
        ),
        migrations.AlterField(
            model_name='food_safety_and_quality',
            name='Composed_manure',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Yes'), ('N', 'No')], default='P', max_length=1, verbose_name='Is composed manure used?'),
        ),
        migrations.AlterField(
            model_name='food_safety_and_quality',
            name='Fertilizer',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Yes'), ('N', 'No')], default='P', max_length=1, verbose_name='Is fertilizer used?'),
        ),
        migrations.AlterField(
            model_name='food_safety_and_quality',
            name='Fertilizer_cont',
            field=models.CharField(max_length=50, null=True, verbose_name='If fertilizer is used, What are they?'),
        ),
        migrations.AlterField(
            model_name='food_safety_and_quality',
            name='Last_application',
            field=models.CharField(max_length=50, null=True, verbose_name='When was the last application of fertilizer'),
        ),
        migrations.AlterField(
            model_name='food_safety_and_quality',
            name='Raw_Manure',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Yes'), ('N', 'No')], default='P', max_length=1, verbose_name='Is raw manure used?'),
        ),
        migrations.AlterField(
            model_name='food_safety_and_quality',
            name='Raw_Manure_cont',
            field=models.CharField(max_length=50, null=True, verbose_name='If raw manure is used, What type?'),
        ),
        migrations.AlterField(
            model_name='inspector_symmary',
            name='estimated_annual_production',
            field=models.CharField(max_length=50, null=True, verbose_name='Enter estimated annual production'),
        ),
        migrations.AlterField(
            model_name='inspector_symmary',
            name='estimated_peak_productions',
            field=models.CharField(max_length=50, null=True, verbose_name='Enter estimated peak production'),
        ),
        migrations.AlterField(
            model_name='policy',
            name='Pesticides',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Yes'), ('N', 'No')], default='P', max_length=1, verbose_name='Was pesticides used?'),
        ),
        migrations.AlterField(
            model_name='policy',
            name='Septic_Tanks',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Yes'), ('N', 'No')], default='P', max_length=1, verbose_name='Are septic tanks used? '),
        ),
        migrations.AlterField(
            model_name='potential_risks',
            name='Chemical_Spills',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Yes'), ('N', 'No')], default='P', max_length=1, verbose_name='Are chemical Spills present?'),
        ),
        migrations.AlterField(
            model_name='potential_risks',
            name='Dumping_of_trash',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Yes'), ('N', 'No')], default='P', max_length=1, verbose_name='Did the dumping of trash occur recently?'),
        ),
        migrations.AlterField(
            model_name='potential_risks',
            name='Feedlot',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Yes'), ('N', 'No')], default='P', max_length=1, verbose_name='Is a feedlot Present?'),
        ),
        migrations.AlterField(
            model_name='potential_risks',
            name='Flooding',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Yes'), ('N', 'No')], default='P', max_length=1, verbose_name='Did flooding occur recently?'),
        ),
        migrations.AlterField(
            model_name='potential_risks',
            name='Heavy_Metal',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Yes'), ('N', 'No')], default='P', max_length=1, verbose_name='Are Heavy Metals present?'),
        ),
        migrations.AlterField(
            model_name='potential_risks',
            name='Slides',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Yes'), ('N', 'No')], default='P', max_length=1, verbose_name='Did land slides occur recently?'),
        ),
        migrations.AlterField(
            model_name='road_access',
            name='Road_Access',
            field=models.CharField(choices=[('', 'Select'), ('Y', 'Yes'), ('N', 'No')], default='P', max_length=1, verbose_name='Is road access available?'),
        ),
    ]