# Generated by Django 4.1.3 on 2022-12-19 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myappstaff', '0016_status_confirm_status_deny_delete_status_rec'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status_confirm',
            old_name='status',
            new_name='status_confirm',
        ),
        migrations.RenameField(
            model_name='status_deny',
            old_name='status',
            new_name='status_deny',
        ),
    ]
