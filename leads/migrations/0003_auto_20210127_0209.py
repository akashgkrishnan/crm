# Generated by Django 3.1.2 on 2021-01-26 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20210124_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_organise',
            field=models.BooleanField(default=True),
        ),
    ]
