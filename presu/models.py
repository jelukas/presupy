from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(blank=True,max_length=255)
    apellidos = models.CharField(blank=True,max_length=255)
    nif = models.CharField(blank=True,max_length=255)
    direccion = models.CharField(blank=True,max_length=255)
    codigo_postal = models.CharField(blank=True,max_length=255)
    localidad = models.CharField(blank=True,max_length=255)
    provincia = models.CharField(blank=True,max_length=255)
    pais = models.CharField(blank=True,max_length=255)
    web = models.CharField(blank=True,max_length=255)
    email = models.CharField(blank=True,max_length=255)
    pais = models.CharField(blank=True,max_length=255)
    telefono = models.CharField(blank=True,max_length=255)
    telefono_movil = models.CharField(blank=True,max_length=255)
    notas = models.TextField(blank=True)

    def __unicode__(self):
        return self.nombre;


class EstadoPresupuesto(models.Model):
    nombre = models.CharField(blank=False,max_length=255)


class Presupuesto(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    numero = models.CharField(blank=False,max_length=255)
    notas = models.TextField(blank=True)
    total = models.DecimalField(max_digits=25, decimal_places=4,default=0)

    cliente = models.ForeignKey(Cliente, related_name='presupuestos')
    estado = models.ForeignKey(EstadoPresupuesto, related_name='presupuestos')

    def codigo(self):
        return self.numero + self.fecha.month + '-' + self.fecha.year

    def neto(self):
        neto = 0;
        for linea in self.lineas:
            neto += linea.neto();
        return neto;

    def total(self):
        total = 0;
        for linea in self.lineas:
            total += linea.total();
        return total;

    def __unicode__(self):
        return self.codigo()


class LineaPresupuesto(models.Model):
    concepto = models.CharField(blank=False,max_length=255)
    candidad = models.DecimalField(max_digits=25, decimal_places=4,default=0)
    precio = models.DecimalField(max_digits=25, decimal_places=4,default=0)
    descuento = models.DecimalField(max_digits=25, decimal_places=4,default=0)
    impuesto = models.DecimalField(max_digits=25, decimal_places=4,default=21)

    presupuesto = models.ForeignKey(Presupuesto, related_name='lineas')

    def neto(self):
        return (self.precio * (1 - self.descuento / 100)) * self.cantidad

    def total(self):
        return self.neto() * (1 - self.impuesto / 100)

    def __unicode__(self):
        return 'Concepto: ' + self.concepto + ' Cantidad: ' + self.candidad + '  Neto: ' + self.neto() + '&euro;'
