# Generated by Django 4.2.3 on 2024-02-11 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcriber_detailes', models.EmailField(max_length=254)),
            ],
        ),
    ]
