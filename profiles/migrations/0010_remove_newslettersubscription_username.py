# Generated by Django 3.2.23 on 2024-02-11 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_newslettersubscription_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newslettersubscription',
            name='username',
        ),
    ]