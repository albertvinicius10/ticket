# Generated by Django 3.2.12 on 2022-10-18 17:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('helpdesk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 10, 18, 17, 5, 25, 571005, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticket',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
