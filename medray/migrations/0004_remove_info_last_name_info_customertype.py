# Generated by Django 4.1.7 on 2023-05-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medray', '0003_alter_info_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='Last_Name',
        ),
        migrations.AddField(
            model_name='info',
            name='CustomerType',
            field=models.CharField(default='patient', max_length=50),
        ),
    ]