# Generated by Django 4.2.1 on 2024-03-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuario_managers_alter_usuario_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
