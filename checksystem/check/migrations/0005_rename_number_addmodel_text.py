# Generated by Django 4.0.5 on 2023-02-18 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0004_addmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addmodel',
            old_name='number',
            new_name='text',
        ),
    ]
