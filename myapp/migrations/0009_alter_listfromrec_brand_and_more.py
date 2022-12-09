# Generated by Django 4.1.3 on 2022-11-29 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_listfromrec_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listfromrec',
            name='brand',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='listfromrec',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='listfromrec',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listfromrec',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='listfromrec',
            name='price',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='listfromrec',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]