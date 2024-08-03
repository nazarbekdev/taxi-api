# Generated by Django 4.2.14 on 2024-08-03 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('direction', models.CharField(max_length=100)),
                ('day', models.CharField(max_length=100)),
                ('hour', models.CharField(max_length=100)),
                ('passengers', models.IntegerField()),
                ('additional_service', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('lan', models.CharField(max_length=50)),
            ],
        ),
    ]
