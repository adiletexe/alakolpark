# Generated by Django 4.0.5 on 2023-02-18 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0002_remove_booking_date_range_remove_booking_room_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('review_text', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')])),
            ],
        ),
    ]
