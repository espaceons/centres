# Generated by Django 5.1.3 on 2024-12-20 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateurs', '0013_customuser_email_verified_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='email_verified',
            new_name='is_email_verified',
        ),
    ]
