# Generated by Django 5.1.3 on 2024-12-13 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('param', '0003_rename_libelle_role_nom'),
        ('utilisateurs', '0006_alter_customuser_centre_alter_customuser_role'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='userProfile',
            new_name='CustomUserProfile',
        ),
    ]
