# Generated by Django 5.1.3 on 2024-12-13 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('param', '0003_rename_libelle_role_nom'),
        ('utilisateurs', '0004_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='centre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='param.centre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='param.role'),
            preserve_default=False,
        ),
    ]
