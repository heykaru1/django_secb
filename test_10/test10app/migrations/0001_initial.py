# Generated by Django 5.0.6 on 2024-06-19 05:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('act_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('act', models.CharField(max_length=55)),
                ('description', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('gender_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=55)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'genders',
            },
        ),
        migrations.CreateModel(
            name='Incomplete',
            fields=[
                ('inc_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('inc', models.CharField(max_length=55)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'incomplete',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=55)),
                ('middle_name', models.CharField(blank=True, max_length=55)),
                ('last_name', models.CharField(max_length=55)),
                ('age', models.IntegerField()),
                ('birth_date', models.DateField()),
                ('username', models.CharField(max_length=55)),
                ('password', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test10app.gender')),
                ('inc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test10app.incomplete')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
