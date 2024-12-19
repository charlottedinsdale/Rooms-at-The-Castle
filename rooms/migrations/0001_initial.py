# Generated by Django 4.2.17 on 2024-12-19 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('number_of_beds', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='RoomAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('availability_status', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable'), ('booked', 'Booked')], max_length=12)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availability', to='rooms.room')),
            ],
        ),
    ]
