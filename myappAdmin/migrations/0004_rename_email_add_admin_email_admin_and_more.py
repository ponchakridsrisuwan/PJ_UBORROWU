# Generated by Django 4.1.3 on 2022-12-02 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myappAdmin', '0003_add_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_admin',
            old_name='email',
            new_name='email_admin',
        ),
        migrations.RenameField(
            model_name='add_staff',
            old_name='email',
            new_name='email_staff',
        ),
        migrations.RenameField(
            model_name='add_user',
            old_name='email',
            new_name='email_user',
        ),
    ]
