# Generated by Django 4.2.5 on 2023-10-23 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_employee_name_id_attendence_employee_name_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
