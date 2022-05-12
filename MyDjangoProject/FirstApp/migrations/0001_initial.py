# Generated by Django 3.2.8 on 2022-05-12 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=254, verbose_name='Name')),
                ('EmployeeID', models.IntegerField(max_length=254, verbose_name='EmpID')),
                ('DateOfJoining', models.DateTimeField(max_length=254, verbose_name='Joining_date')),
            ],
        ),
    ]
