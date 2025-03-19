from django.contrib import admin
from . import models
from . import forms

# Register your models here.

class TareaAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        # Creación de tarea
        if not obj:  
            return forms.TareaFormCreacion
        # Edición de tarea
        else:  
            return forms.TareaFormEdicion

    #filtro
    list_filter = ('id_estado',)
    #personalizacion de campos visualizados
    list_display = ('id_tarea', 'id_proyecto','usuario_rol','titulo')


class ProyectoUsuarioRolAdmin(admin.ModelAdmin):
    #personalizacion de campos visualizados
    list_display = ('proyecto_nombre', 'rol_nombre', 'usuario_nombre', 'estado')   
    #busquedapor: nombre de proyecto, rol, y usuario
    search_fields = ('id_proyecto__titulo', 'id_rol__name', 'id_user__username') 

admin.site.register(models.Proyecto)
admin.site.register(models.Tarea, TareaAdmin)
admin.site.register(models.ProyectoUsuarioRol, ProyectoUsuarioRolAdmin)
admin.site.register(models.EstadoTarea)
