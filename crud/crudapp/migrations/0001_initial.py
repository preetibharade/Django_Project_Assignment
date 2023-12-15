# Generated by Django 5.0 on 2023-12-14 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'City',
            },
        ),
        migrations.CreateModel(
            name='Educationlevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_level', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Educationlevel',
            },
        ),
        migrations.CreateModel(
            name='Employeedirectory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referred_by', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Employeedirectory',
            },
        ),
        migrations.CreateModel(
            name='Eventdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(blank=True, max_length=255, null=True)),
                ('event_date', models.DateTimeField(blank=True, null=True)),
                ('event_location', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'EventDetails',
            },
        ),
        migrations.CreateModel(
            name='Experiencelevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_level', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Experiencelevel',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Gender',
            },
        ),
        migrations.CreateModel(
            name='Jobrequisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_position', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Jobrequisition',
            },
        ),
        migrations.CreateModel(
            name='Maritalstatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marital_status', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Maritalstatus',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona', models.CharField(blank=True, default=1, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Persona',
            },
        ),
        migrations.CreateModel(
            name='Reasonforchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_for_change', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Reasonforchange',
            },
        ),
        migrations.CreateModel(
            name='Screeningmode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screening_mode', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Screeningmode',
            },
        ),
    ]
