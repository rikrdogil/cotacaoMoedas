# Generated by Django 4.0.3 on 2022-03-19 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('base', models.CharField(max_length=3)),
                ('rate', models.CharField(max_length=3)),
                ('valor', models.FloatField()),
            ],
        ),
    ]
