# Generated by Django 5.1.7 on 2025-03-19 17:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadotarea',
            name='estado',
            field=models.BooleanField(db_comment='ESTADO ACTIVO O INACTIVO', default=True),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='estado',
            field=models.BooleanField(db_comment='ESTADO ACTIVO O INACTIVO', default=True),
        ),
        migrations.AlterField(
            model_name='proyectousuariorol',
            name='estado',
            field=models.BooleanField(db_comment='ESTADO ACTIVO O INACTIVO', default=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='id_estado',
            field=models.ForeignKey(db_column='id_estado', db_comment='IDENTIFICADOR DE LA TAREA.', default=1, on_delete=django.db.models.deletion.CASCADE, to='app.estadotarea', verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='id_proyecto',
            field=models.ForeignKey(db_column='id_proyecto', db_comment='IDENTIFICADOR DEL PROYECTO', on_delete=django.db.models.deletion.CASCADE, to='app.proyecto', verbose_name='Proyecto'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='usuario_rol',
            field=models.ForeignKey(blank=True, db_comment='USUARIO ASIGNADO A LA TAREA', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
