# Generated by Django 3.1.7 on 2022-04-28 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0003_auto_20220428_1328'),
        ('joffeedapp', '0006_auto_20220428_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jof',
            name='artist',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Artist', to='loginapp.account'),
        ),
    ]
