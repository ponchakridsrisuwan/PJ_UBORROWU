# Generated by Django 4.1.3 on 2022-11-27 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Durable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(blank=True, max_length=300, null=True)),
                ('quantity', models.CharField(blank=True, max_length=200, null=True)),
                ('numdate', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='posts')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Add_Parcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(blank=True, max_length=300, null=True)),
                ('quantity', models.CharField(blank=True, max_length=200, null=True)),
                ('numdate', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='posts')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
