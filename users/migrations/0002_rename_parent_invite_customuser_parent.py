# Generated by Django 4.2.4 on 2023-08-21 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='parent_invite',
            new_name='parent',
        ),
    ]
