# Generated by Django 2.0.9 on 2018-11-07 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmc', '0004_auto_20181107_1103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='created_emp',
            new_name='employee',
        ),
    ]
