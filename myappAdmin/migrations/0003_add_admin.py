# Generated by Django 4.1.3 on 2022-12-02 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappAdmin', '0002_add_user_rename_add_actor_add_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Admin',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=bool, serialize=False)),
            ],
        ),
    ]
