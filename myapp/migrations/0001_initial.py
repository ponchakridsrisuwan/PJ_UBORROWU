# Generated by Django 4.1.3 on 2022-11-27 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListRec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('brand', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.CharField(max_length=64)),
                ('price', models.FloatField()),
                ('link', models.URLField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]