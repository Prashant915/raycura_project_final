# Generated by Django 4.1.7 on 2023-05-15 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medray', '0008_alter_customer_information_customertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='display_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paste_link', models.TextField(max_length=300)),
            ],
        ),
    ]