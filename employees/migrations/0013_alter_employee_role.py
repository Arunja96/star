# Generated by Django 4.2.5 on 2023-10-16 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
        ('employees', '0012_alter_employee_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='roles.role'),
        ),
    ]
