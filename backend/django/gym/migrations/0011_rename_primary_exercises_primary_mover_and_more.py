# Generated by Django 4.2.7 on 2024-02-07 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0010_alter_user_email_alter_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercises',
            old_name='primary',
            new_name='primary_mover',
        ),
        migrations.RenameField(
            model_name='exercises',
            old_name='secondary',
            new_name='secondary_mover',
        ),
    ]