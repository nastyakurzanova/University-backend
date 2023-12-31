# Generated by Django 4.2.4 on 2023-10-24 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('role', models.CharField()),
                ('phone', models.FloatField()),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
