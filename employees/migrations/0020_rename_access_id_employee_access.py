# Generated by Django 4.2.5 on 2023-10-24 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0019_remove_employee_created_by_employee_access_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='access_id',
            new_name='access',
        ),
    ]
