# Generated by Django 3.2.8 on 2021-10-24 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alcohol', '0004_auto_20211020_2318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='for_anonimous_user',
            new_name='for_anonymous_user',
        ),
    ]
