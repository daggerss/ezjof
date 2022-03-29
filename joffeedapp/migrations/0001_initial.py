# Generated by Django 3.1.7 on 2022-03-28 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JOF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('blastdate', models.DateField()),
                ('shortdesc', models.CharField(default='', max_length=100)),
                ('jobspecs', models.CharField(default='', max_length=100)),
                ('spiel', models.CharField(default='', max_length=100)),
                ('ispending', models.BooleanField()),
                ('isrush', models.BooleanField()),
                ('isarchive', models.BooleanField()),
            ],
        ),
    ]
