# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User, Group


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         db_table = 'django_session'


class EstadoTarea(models.Model):
    id_estado = models.BigAutoField(primary_key=True, db_comment='IDENTIFICADOR DE LA TAREA.')
    nombre_estado = models.CharField(db_comment='NOMBRE DEL ESTADO')
    descripcion_estado = models.CharField(blank=True, null=True, db_comment='DESCRIPCION DEL ESTADO DE LA TAREA')
    estado = models.BooleanField(db_comment='ESTADO ACTIVO O INACTIVO')

    class Meta:
        db_table = 'estado_tarea'
        db_table_comment = 'ESTADO DE LA TAREA'


class Proyecto(models.Model):
    id_proyecto = models.BigAutoField(primary_key=True, db_comment='IDENTIFICADOR DEL PROYECTO')
    fecha_creacion = models.DateField(db_comment='FECHA DE CREACION DEL PROYECTO')
    titulo = models.CharField(db_comment='TITULO DEL PROYECTO')
    estado = models.BooleanField(db_comment='ESTADO ACTIVO O INACTIVO')

    class Meta:
        db_table = 'proyecto'
        db_table_comment = 'TABLA DONDE SE ALMACENA LOS PROYECTOS'


class ProyectoUsuarioRol(models.Model):
    id_proyecto_usuario_rol = models.BigAutoField(primary_key=True, db_comment='IDENTIFDICADOR DE LA RELACION ENTRE LAS TABLAS PROYECTO, ROL, USUARIO')
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, db_column='id_proyecto', db_comment='IDENTIFICADOR DEL PROYECTO')
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='id_user', db_comment='IDENTIFICADOR DEL USUARIO')
    id_rol = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='id_group', db_comment='IDENTIFICADOR DEL ROL')
    estado = models.BooleanField(db_comment='ESTADO ACTIVO O INACTIVO')

    class Meta:
        db_table = 'proyecto_usuario_rol'
        db_table_comment = 'TABLA DONDE SE INDICA QUE USUARIO ESTA RELACIONADO CON CADA PROYECTO, Y EL ROL QUE TENDRA'


class Tarea(models.Model):
    id_tarea = models.BigAutoField(primary_key=True, db_comment='IDENTIFICADOR DE LA TAREA')
    id_estado = models.ForeignKey(EstadoTarea, on_delete=models.CASCADE, db_column='id_estado', db_comment='IDENTIFICADOR DE LA TAREA.')
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, db_column='id_proyecto', db_comment='IDENTIFICADOR DEL PROYECTO')
    usuario_rol = models.CharField(blank=True, null=True, db_comment='USUARIO ASIGNADO A LA TAREA')
    titulo = models.CharField(db_comment='TITULO DE LA TAREA')
    descripcion = models.CharField(db_comment='DESCRIPCION DE LA TAREA')
    comentario = models.CharField(blank=True, null=True, db_comment='COMENTARIO DE LA TAREA')
    fecha_inicio_estimada = models.DateField(db_comment='FECHA ESTIMADA DE INICIO')
    fecha_fin_estimada = models.DateField(db_comment='FECHA ESTIMADA DE FIN')
    fecha_inicio_real = models.DateField(blank=True, null=True, db_comment='FECHA REAL DE INICIO')
    fecha_fin_real = models.DateField(blank=True, null=True, db_comment='FECHA REAL DE FIN')

    class Meta:
        db_table = 'tarea'
        db_table_comment = 'TABLA DE LAS TAREAS RELACIONADAS A UN PROYECTO'



