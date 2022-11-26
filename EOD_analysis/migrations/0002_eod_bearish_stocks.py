# Generated by Django 3.1.4 on 2021-01-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EOD_analysis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EOD_bearish_stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('symbol', models.CharField(max_length=50)),
                ('strategy', models.CharField(max_length=100)),
            ],
        ),
    ]