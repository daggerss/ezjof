# Generated by Django 3.1.7 on 2022-03-14 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0003_auto_20220314_1429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='account',
            name='mname',
        ),
    ]
