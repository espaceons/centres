# Generated by Django 5.1.3 on 2024-12-09 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateurs', '0002_customuser_centre_alter_customuser_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='follows',
        ),
    ]