from django.contrib import admin

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from presu.models import Cliente
from presu.models import Presupuesto
from presu.models import LineaPresupuesto
from presu.models import EstadoPresupuesto


class LineaPresupuestoInline(admin.TabularInline):
    model = LineaPresupuesto
    extra = 2;

class PresupuestoAdmin(admin.ModelAdmin):
    fields = [('codigo', 'numero','fecha'),'cliente','estado','notas','neto','impuestos','total',]
    readonly_fields = ['total','codigo','neto','impuestos',]
    list_display = ['codigo','fecha', 'numero','cliente','estado','notas','neto','impuestos','total',]
    list_editable = ['estado']

    # define the raw_id_fields
    raw_id_fields = ('cliente',)
    # define the related_lookup_fields
    autocomplete_lookup_fields = {
        'fk': ['cliente'],
    }

    search_fields = ['numero','cliente__nombre']
    list_filter = ('fecha','estado')

    inlines = [LineaPresupuestoInline,]

    "Cargamos el Javavscript que usaremos para recarlcular los totales en tiempo real"
    class Media:
        js = ("js/presupy.js",)
        css = {
            "all": ("css/presupuesto_change.css",)
        }

    """Esto hara que cuando editemos y guardemos vayamos de nuevo a la pagina de edicion y no a la lista de presupuestos"""
    def response_change(self, request, obj):
        """This makes the response go to the newly created model's change page
        without using reverse"""
        return HttpResponseRedirect(request.path)

class LineaPresupuestoAdmin(admin.ModelAdmin):
    list_display = ['concepto','cantidad', 'precio','descuento','impuesto','total','presupuesto','presupuesto_link',]
    list_select_related = True

    "Para que muestre el enlace en una Foreing Key en la lista"
    def presupuesto_link(self, obj):
        url = reverse('admin:presu_presupuesto_change', args=(obj.presupuesto.pk,))
        return '<a href="%s">%s</a>' % (url,obj.presupuesto.codigo())
    presupuesto_link.allow_tags = True


"""
Registro de los modelos de Adminsitracion
"""
admin.site.register(Cliente)
admin.site.register(Presupuesto,PresupuestoAdmin)
admin.site.register(LineaPresupuesto,LineaPresupuestoAdmin)
admin.site.register(EstadoPresupuesto)
