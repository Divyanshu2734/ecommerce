# Generated by Django 4.2.3 on 2023-11-29 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frist_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mob', models.IntegerField()),
                ('address', models.TextField(max_length=300)),
                ('query', models.TextField(max_length=500)),
            ],
        ),
    ]