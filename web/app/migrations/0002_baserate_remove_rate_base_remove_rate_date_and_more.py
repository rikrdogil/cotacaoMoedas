# Generated by Django 4.0.3 on 2022-03-24 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('base', models.CharField(max_length=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='rate',
            name='base',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='date',
        ),
        migrations.AddField(
            model_name='rate',
            name='codigo_date_rate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.baserate'),
        ),
    ]