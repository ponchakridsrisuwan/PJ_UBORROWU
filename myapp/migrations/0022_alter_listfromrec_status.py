# Generated by Django 4.1.3 on 2022-12-19 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_listfromrec_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listfromrec',
            name='status',
            field=models.CharField(default=False, max_length=300, null=True),
        ),
    ]
