# Generated by Django 3.2.12 on 2022-10-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, null=True)),
                ('prioridade', models.CharField(choices=[('Alta', 'Alta'), ('Baixa', 'Baixa'), ('Moderada', 'Moderada')], max_length=20, null=True)),
                ('descricao', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'ticket',
            },
        ),
    ]
