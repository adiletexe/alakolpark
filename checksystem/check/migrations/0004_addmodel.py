# Generated by Django 4.0.5 on 2023-02-18 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0003_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.TextField()),
                ('phone', models.IntegerField(max_length=14)),
            ],
        ),
    ]