# Generated by Django 4.2.5 on 2023-10-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_employee_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone_no',
            field=models.IntegerField(verbose_name='Phone No'),
        ),
    ]