from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # Esto calca el orden de tu foto de Dynamics
    list_display = (
        'codigo_bc', 
        'nombre', 
        'alias', 
        'direccion_2', 
        'cif_nif', 
        'saldo', 
        'saldo_periodo', 
        'departamento_code', 
        'direccion'
    )

    search_fields = ('codigo_bc', 'nombre', 'cif_nif', 'alias')
    list_filter = ('departamento_code', 'bloqueado')

    fieldsets = (
        ('General', {
            'fields': (
                'codigo_bc', 
                'nombre', 
                ('cif_nif', 'alias'), 
                'direccion', 
                'direccion_2',
                ('saldo', 'departamento_code'),
            )
        }),
        ('Comunicación', {
            'fields': (('telefono', 'contacto'),),
        }),
        ('Facturación', {
            'fields': ('saldo_periodo',),
        }),
        ('Otros', {
            'fields': ('cod_almacen', 'centro_responsabilidad', 'bloqueado'),
        }),
    )