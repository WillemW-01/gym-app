# Generated by Django 4.2.7 on 2024-02-07 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0011_rename_primary_exercises_primary_mover_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]