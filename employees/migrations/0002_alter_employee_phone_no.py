# Generated by Django 4.2.5 on 2023-10-13 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone_no',
            field=models.IntegerField(max_length=100, verbose_name='Phone No'),
        ),
    ]