# Generated by Django 3.2.8 on 2022-05-12 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='EmployeeID',
            field=models.IntegerField(verbose_name='EmpID'),
        ),
    ]
