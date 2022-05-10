# Generated by Django 4.0.3 on 2022-05-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joffeedapp', '0008_jof_department_alter_jof_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jof',
            name='status',
            field=models.IntegerField(choices=[(1, 'Is Pending'), (2, 'In Progress'), (3, 'Not Taken'), (4, 'Is Completed')], default=3),
        ),
    ]
