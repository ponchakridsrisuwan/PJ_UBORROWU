# Generated by Django 4.1.3 on 2022-11-27 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_listrec_link_alter_listrec_quantity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ListRec',
            new_name='ListFromRec',
        ),
    ]
