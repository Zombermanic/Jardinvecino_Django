# Generated by Django 4.2.1 on 2023-07-06 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JardinVecino', '0003_usuario_comuna_usuario_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
    ]
