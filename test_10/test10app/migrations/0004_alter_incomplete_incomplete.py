# Generated by Django 5.0.6 on 2024-06-19 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test10app', '0003_rename_inc_user_incomplete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomplete',
            name='incomplete',
            field=models.CharField(blank=True, max_length=55),
        ),
    ]
