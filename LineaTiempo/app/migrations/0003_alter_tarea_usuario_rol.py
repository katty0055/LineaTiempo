# Generated by Django 5.1.7 on 2025-03-19 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_estadotarea_estado_alter_proyecto_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='usuario_rol',
            field=models.CharField(blank=True, db_comment='USUARIO ASIGNADO A LA TAREA', null=True),
        ),
    ]
