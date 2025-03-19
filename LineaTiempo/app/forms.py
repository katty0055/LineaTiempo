from django import forms
from .models import Tarea, ProyectoUsuarioRol
from django.contrib.admin import widgets
from django.core.exceptions import ValidationError


class TareaFormBase(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'
        widgets = {
            'fecha_inicio_estimada': widgets.AdminDateWidget(),
            'fecha_fin_estimada': widgets.AdminDateWidget(),
            'fecha_inicio_real': widgets.AdminDateWidget(),
            'fecha_fin_real': widgets.AdminDateWidget(),
        }

    def clean(self):
        cleaned_data = super().clean()
        
        fecha_inicio_estimada = cleaned_data.get('fecha_inicio_estimada')
        fecha_fin_estimada = cleaned_data.get('fecha_fin_estimada')
        fecha_inicio_real = cleaned_data.get('fecha_inicio_real')
        fecha_fin_real = cleaned_data.get('fecha_fin_real')

        # Validar que la fecha de inicio estimada no sea posterior a la fecha de fin estimada
        if fecha_inicio_estimada and fecha_fin_estimada:
            if fecha_inicio_estimada > fecha_fin_estimada:
                raise ValidationError("La fecha de inicio estimada no puede ser posterior a la fecha de fin estimada.")
        
        # Validar que la fecha de inicio real no sea posterior a la fecha de fin real
        if fecha_inicio_real and fecha_fin_real:
            if fecha_inicio_real > fecha_fin_real:
                raise ValidationError("La fecha de inicio real no puede ser posterior a la fecha de fin real.")
        
        
        # Validar que la fecha de finalización real no sea anterior a la fecha de inicio real
        if fecha_fin_real and fecha_inicio_real:
            if fecha_fin_real < fecha_inicio_real:
                raise ValidationError("La fecha de finalización real no puede ser anterior a la fecha de inicio real.")
        
        return cleaned_data


class TareaFormCreacion(TareaFormBase):
    class Meta:
        model = Tarea
        #Excluye los campos
        exclude = ('id_estado','usuario_rol','comentario','fecha_inicio_real','fecha_fin_real')  
        widgets = {
            **TareaFormBase.Meta.widgets, 
        }


class TareaFormEdicion(TareaFormBase):
    usuario_rol = forms.ChoiceField(choices=[], required=False)

    class Meta:
        model = Tarea
        fields = '__all__'
        widgets = {
           **TareaFormBase.Meta.widgets, 
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Establecer ciertos campos como solo lectura
        self.fields['id_proyecto'].widget = forms.TextInput(attrs={'readonly': 'readonly'})
        self.fields['id_estado'].widget = forms.TextInput(attrs={'readonly': 'readonly'})
        self.fields['fecha_inicio_estimada'].widget = forms.TextInput(attrs={'readonly': 'readonly'})
        self.fields['fecha_fin_estimada'].widget = forms.TextInput(attrs={'readonly': 'readonly'})
        # self.fields['id_proyecto'].widget = forms.TextInput(attrs={'readonly': 'readonly', 'value': self.instance.id_proyecto.titulo})

        #Filtrar usuarios del proyecto
        if self.instance and hasattr(self.instance, 'id_proyecto') and self.instance.id_proyecto:
            usuarios_proyecto = ProyectoUsuarioRol.objects.filter(id_proyecto=self.instance.id_proyecto)
            opciones = [(str(u.id_user), u.id_user) for u in usuarios_proyecto]
            opciones.insert(0, ("", "---------"))
            self.fields['usuario_rol'].choices = opciones


        