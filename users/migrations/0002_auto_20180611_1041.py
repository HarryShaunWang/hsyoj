# Generated by Django 2.0.6 on 2018-06-11 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('view_all_users', "View all users' information."),)},
        ),
    ]
