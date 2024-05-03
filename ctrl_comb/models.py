from django.db import models

class Mark(models.Model):
    descript = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return  self.descript
    
    class Meta: 
        verbose_name='Marca'
        verbose_name_plural='Marcas'

class Modelo(models.Model):
    descript = models.CharField(
        max_length=200,
        #db_comment = 'Descripcion del modelo'
        unique=True)
    
    mark = models.ForeignKey(Mark,
                             on_delete = models.PROTECT)

    def __str__(self):
        return f"{self.mark} - {self.descript}"
    
    class Meta: 
        verbose_name_plural='Modelos'
        #db_table_comment = 'Modelos de vehiculos'
