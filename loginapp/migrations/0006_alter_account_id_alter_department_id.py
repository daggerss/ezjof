# Generated by Django 4.0.3 on 2022-03-15 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0005_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
