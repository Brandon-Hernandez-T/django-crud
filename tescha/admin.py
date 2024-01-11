from django.contrib import admin
from .models import Inscripcion, Curso, Estudiante


@admin.register(Curso)
class CursosAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'descripcion',
        'creditos',
        'horario',
        'cupo',
        'maestro'
    ]

    search_fields = ['name', 'maestro']

@admin.register(Estudiante)
class CursosAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'matricula'
    ]

    search_fields = ['matricula']

@admin.register(Inscripcion)
class CursosAdmin(admin.ModelAdmin):
    list_display = [
        # 'estudiante',
        'estudiante_info',
        'cruso',
        'fecha_inscripcion'
    ]

    def estudiante_info(self, obj):
        return f"{obj.estudiante.nombre} ({obj.estudiante.matricula})"

    search_fields = ['fecha_inscripcion']
