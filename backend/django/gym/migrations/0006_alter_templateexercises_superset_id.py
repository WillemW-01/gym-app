# Generated by Django 4.2.7 on 2024-01-29 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0005_alter_templates_lastperformed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templateexercises',
            name='superset_id',
            field=models.IntegerField(null=True),
        ),
    ]
