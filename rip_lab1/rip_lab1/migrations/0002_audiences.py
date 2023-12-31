# Generated by Django 4.2.4 on 2023-10-24 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rip_lab1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audiences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('image', models.CharField(max_length=100)),
                ('info', models.FloatField()),
                ('status', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Аудитория',
                'verbose_name_plural': 'Аудитории',
                'db_table': 'audiences',
                'managed': False,
            },
        ),
    ]
