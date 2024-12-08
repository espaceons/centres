# Generated by Django 5.1.3 on 2024-12-09 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('param', '0001_initial'),
        ('utilisateurs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='centre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='role', to='param.centre'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='role', to='param.role'),
        ),
    ]
