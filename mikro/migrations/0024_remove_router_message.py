# Generated by Django 4.2 on 2023-05-14 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mikro', '0023_router_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='router',
            name='message',
        ),
    ]
