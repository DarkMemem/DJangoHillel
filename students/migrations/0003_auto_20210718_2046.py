# Generated by Django 3.2.4 on 2021-07-18 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_students_groups_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='email',
            field=models.EmailField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='first_name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='students',
            name='last_name',
            field=models.CharField(max_length=80),
        ),
    ]
