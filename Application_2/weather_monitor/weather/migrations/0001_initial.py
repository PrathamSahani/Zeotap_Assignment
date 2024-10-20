# Generated by Django 5.1.2 on 2024-10-19 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyWeatherSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('average_temp', models.FloatField()),
                ('max_temp', models.FloatField()),
                ('min_temp', models.FloatField()),
                ('dominant_condition', models.CharField(max_length=50)),
            ],
        ),
    ]