# Generated by Django 5.1 on 2024-11-02 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('sno', models.IntegerField(primary_key=True, serialize=False)),
                ('note', models.CharField(max_length=200)),
            ],
        ),
    ]
