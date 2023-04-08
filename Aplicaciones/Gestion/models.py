from django.db import models


# Create your models here.

class Cez(models.Model):
    codigo = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)


class Comcorr(models.Model):
    nombre = models.CharField(max_length=120)


class Barrver(models.Model):
    nombre = models.CharField(max_length=120)
    nomcomun = models.CharField(max_length=120)


class Persona(models.Model):
    identificacion = models.CharField(primary_key=True, max_length=120)
    nombres = models.CharField(max_length=40)
    apellido1 = models.CharField(max_length=40)
    apellido2 = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=40)

    @property
    def nombrecompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellido1, self.apellido2, self.nombres)


class PersonaDiger(models.Model):
    identificacion = models.CharField(primary_key=True, max_length=120)
    nombres = models.CharField(max_length=40)
    apellido1 = models.CharField(max_length=40)
    apellido2 = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=40)

    def nombrecompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellido1, self.apellido2, self.nombres)


class Geologia(models.Model):
    unidad = models.CharField(max_length=40)
    peso = models.FloatField()
    leyenda = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=120)


class Litologia(models.Model):
    unidad = models.CharField(max_length=120)
    peso = models.FloatField()
    leyenda = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=120)


class Pendiente(models.Model):
    rango = models.CharField(max_length=40)
    categoria = models.CharField(max_length=40)
    peso = models.FloatField()
    descripcion = models.CharField(max_length=120)


class Freatico(models.Model):
    posicion = models.CharField(max_length=40)
    peso = models.FloatField()
    descripcion = models.CharField(max_length=120)


class Erosion(models.Model):
    tipoerosion = models.CharField(max_length=80)
    peso = models.FloatField()
    descripcion = models.CharField(max_length=120)


class Deslizamiento(models.Model):
    tipodeslizam = models.CharField(max_length=80)
    peso = models.FloatField()
    descripcion = models.CharField(max_length=120)


class ElemExpuestos(models.Model):
    elemexpuestos = models.CharField(max_length=80)
    peso = models.FloatField()
    descripcion = models.CharField(max_length=120)


class Afectacion(models.Model):
    afectacion = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=120)


class Cobertura(models.Model):
    cobertura = models.CharField(max_length=40)
    peso = models.FloatField()
    descripcion = models.CharField(max_length=120)


class Tipoactividad(models.Model):
    actividad = models.CharField(max_length=40)
    peso = models.FloatField()
    descripcion = models.CharField(max_length=120)


class Tipoproceso(models.Model):
    tipo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=120)


class TipoTalud(models.Model):
    tipo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=120)


class Tipoclima(models.Model):
    clima = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=120)


class FactoresContr(models.Model):
    fcontribuyente = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=120)


class FactoresDeton(models.Model):
    fdetonante = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=120)


class Obras(models.Model):
    obra = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=120)


class Psicos(models.Model):
    psico = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=120)


class Taludes(models.Model):
    cez = models.ForeignKey(Cez, null=False, blank=False, on_delete=models.CASCADE)
    comcorr = models.ForeignKey(Comcorr, null=False, blank=False, on_delete=models.CASCADE)
    barrver = models.ForeignKey(Barrver, null=False, blank=False, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=120)
    latitud = models.FloatField
    longitud = models.FloatField
    geologia = models.ForeignKey(Geologia, null=False, blank=False, on_delete=models.CASCADE)
    litologia = models.ForeignKey(Litologia, null=False, blank=False, on_delete=models.CASCADE)
    persocontacto = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
    largo = models.FloatField
    alto = models.FloatField
    pendiente = models.ForeignKey(Pendiente, null=False, blank=False, on_delete=models.CASCADE)
    tipotalud = models.ForeignKey(TipoTalud, null=False, blank=False, on_delete=models.CASCADE)
    observaciones = models.CharField(500)
    foto1 = models.URLField(max_length=500)
    foto2 = models.URLField(max_length=500)
    foto3 = models.URLField(max_length=500)
    url_datos = models.URLField(max_length=500)


class VisitasTalud(models.Model):
    fecha = models.DateField()
    talud = models.ForeignKey(Taludes, null=False, blank=False, on_delete=models.CASCADE)
    personadiger = models.ForeignKey(PersonaDiger, null=False, blank=False, on_delete=models.CASCADE)
    tipoerosion = models.ForeignKey(Erosion, null=False, blank=False, on_delete=models.CASCADE)
    tipodeslizam = models.ForeignKey(Deslizamiento, null=False, blank=False, on_delete=models.CASCADE)
    tipoproceso = models.ForeignKey(Tipoproceso, null=False, blank=False, on_delete=models.CASCADE)
    cobersuelo = models.ForeignKey(Cobertura, null=False, blank=False, on_delete=models.CASCADE)
    tipoactiv = models.ForeignKey(Tipoactividad, null=False, blank=False, on_delete=models.CASCADE)
    clima = models.ForeignKey(Tipoclima, null=False, blank=False, on_delete=models.CASCADE)
    freatico = models.ForeignKey(Freatico, null=False, blank=False, on_delete=models.CASCADE)
    elemexpuestos = models.ForeignKey(ElemExpuestos, null=False, blank=False, on_delete=models.CASCADE)
    detonante = models.ForeignKey(FactoresDeton, null=False, blank=False, on_delete=models.CASCADE)
    contribuyente = models.ForeignKey(FactoresContr, null=False, blank=False, on_delete=models.CASCADE)
    afectacion = models.ForeignKey(Afectacion, null=False, blank=False, on_delete=models.CASCADE)
    obrasrecomend = models.ForeignKey(Obras, null=False, blank=False, on_delete=models.CASCADE)
    psicorecomend = models.ForeignKey(Psicos, null=False, blank=False, on_delete=models.CASCADE)
    observaciones = models.CharField(500)
    foto1 = models.URLField(max_length=500)
    foto2 = models.URLField(max_length=500)
    foto3 = models.URLField(max_length=500)
