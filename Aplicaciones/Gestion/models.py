from django.db import models

# Create your models here.

class Cez(models.Model):
    codigo = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=40,null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.nombre)

class Comcorr(models.Model):
    nombre = models.CharField(max_length=120,null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.nombre)


class Barrver(models.Model):
    nombre = models.CharField(max_length=120,null=False, blank=False)
    nomcomun = models.CharField(max_length=120)

    def __str__(self):
        return "{0}".format(self.nombre)


class Persona(models.Model):
    identificacion = models.CharField(primary_key=True, max_length=20)
    nombres = models.CharField(max_length=40,null=False, blank=False)
    apellido1 = models.CharField(max_length=40,null=False, blank=False)
    apellido2 = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10,null=False, blank=False)
    email = models.CharField(max_length=40)


    def nombrecompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellido1, self.apellido2, self.nombres)

    def __str__(self):
        return self.nombrecompleto()


class PersonaDiger(models.Model):
    identificacion = models.CharField(primary_key=True, max_length=20)
    nombres = models.CharField(max_length=40,null=False, blank=False)
    apellido1 = models.CharField(max_length=40,null=False, blank=False)
    apellido2 = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10,null=False, blank=False)
    email = models.CharField(max_length=40,null=False, blank=False)


    def nombrecompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellido1, self.apellido2, self.nombres)

    def __str__(self):
        return self.nombrecompleto()


class Geologia(models.Model):
    unidad = models.CharField(max_length=40, null=False, blank=False)
    peso = models.FloatField(null=False, blank=False)
    leyenda = models.CharField(max_length=120, null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.unidad)


class Litologia(models.Model):
    unidad = models.CharField(max_length=120, null=False, blank=False)
    peso = models.FloatField(null=False, blank=False)
    leyenda = models.CharField(max_length=120, null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.unidad)


class Pendiente(models.Model):
    rango = models.CharField(max_length=40, null=False, blank=False)
    categoria = models.CharField(max_length=40, null=False, blank=False)
    peso = models.FloatField(null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.rango)


class Freatico(models.Model):
    posicion = models.CharField(max_length=40, null=False, blank=False)
    peso = models.FloatField(null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.posicion)


class Erosion(models.Model):
    tipoerosion = models.CharField(max_length=80, null=False, blank=False)
    peso = models.FloatField(null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.tipoerosion)


class Deslizamiento(models.Model):
    tipodeslizam = models.CharField(max_length=80, null=False, blank=False)
    peso = models.FloatField(null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.tipodeslizam)


class ElemExpuestos(models.Model):
    elemexpuestos = models.CharField(max_length=80, null=False, blank=False)
    peso = models.FloatField(null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.elemexpuestos)


class Afectacion(models.Model):
    afectacion = models.CharField(max_length=80, null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.afectacion)


class Cobertura(models.Model):
    cobertura = models.CharField(max_length=40, null=False, blank=False)
    peso = models.FloatField(null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.cobertura)


class TipoActividad(models.Model):
    actividad = models.CharField(max_length=40, null=False, blank=False)
    peso = models.FloatField(null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.actividad)

class TipoProceso(models.Model):
    tipo = models.CharField(max_length=40, null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.tipo)


class TipoTalud(models.Model):
    tipo = models.CharField(max_length=40, null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.tipo)


class TipoClima(models.Model):
    clima = models.CharField(max_length=40, null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.clima)


class FactoresContr(models.Model):
    fcontribuyente = models.CharField(max_length=40, null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.fcontribuyente)


class FactoresDeton(models.Model):
    fdetonante = models.CharField(max_length=40, null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.fdetonante)


class Obras(models.Model):
    obra = models.CharField(max_length=40, null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.obra)


class Psicos(models.Model):
    psico = models.CharField(max_length=40, null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.psico)


class Taludes(models.Model):
    cez = models.ForeignKey(Cez, null=False, blank=False, on_delete=models.CASCADE)
    comcorr = models.ForeignKey(Comcorr, null=False, blank=False, on_delete=models.CASCADE)
    barrver = models.ForeignKey(Barrver, null=False, blank=False, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=120)
    latitud = models.FloatField(null=False, blank=False)
    longitud = models.FloatField(null=False, blank=False)
    geologia = models.ForeignKey(Geologia, null=False, blank=False, on_delete=models.CASCADE)
    litologia = models.ForeignKey(Litologia, null=False, blank=False, on_delete=models.CASCADE)
    persocontacto = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
    largo = models.FloatField(null=False, blank=False)
    alto = models.FloatField(null=False, blank=False)
    pendiente = models.ForeignKey(Pendiente, null=False, blank=False, on_delete=models.CASCADE)
    tipotalud = models.ForeignKey(TipoTalud, null=False, blank=False, on_delete=models.CASCADE)
    observaciones = models.CharField(max_length=500)
    foto1 = models.URLField(max_length=500)
    foto2 = models.URLField(max_length=500)
    foto3 = models.URLField(max_length=500)
    url_datos = models.URLField(max_length=500)


class VisitasTalud(models.Model):
    fecha = models.DateField(null=False, blank=False)
    talud = models.ForeignKey(Taludes, null=False, blank=False, on_delete=models.CASCADE)
    personadiger = models.ForeignKey(PersonaDiger, null=False, blank=False, on_delete=models.CASCADE)
    tipoerosion = models.ForeignKey(Erosion, null=False, blank=False, on_delete=models.CASCADE)
    tipodeslizam = models.ManyToManyField(Deslizamiento)
    TipoProceso = models.ForeignKey(TipoProceso, null=False, blank=False, on_delete=models.CASCADE)
    cobersuelo = models.ManyToManyField(Cobertura)
    tipoactiv = models.ForeignKey(TipoActividad, null=False, blank=False, on_delete=models.CASCADE)
    clima = models.ForeignKey(TipoClima, null=False, blank=False, on_delete=models.CASCADE)
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