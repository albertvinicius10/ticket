# Generated by Django 4.1.2 on 2022-10-21 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0007_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
