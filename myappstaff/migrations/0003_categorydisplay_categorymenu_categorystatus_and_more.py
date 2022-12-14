# Generated by Django 4.1.3 on 2022-11-30 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappstaff', '0002_alter_add_durable_image_alter_add_parcel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryDisplay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_CategoryDisplay', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_CategoryMenu', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_CategoryStatus', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_CategoryType', models.CharField(max_length=100)),
            ],
        ),
    ]
