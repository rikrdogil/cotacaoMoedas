# Generated by Django 4.0.3 on 2022-03-25 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_baserate_remove_rate_base_remove_rate_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='codigo_date_rate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='base_rate', to='app.baserate'),
        ),
    ]
