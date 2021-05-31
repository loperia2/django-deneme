from django.db import models
from autoslug import AutoSlugField

class categoryModel(models.Model):
    isim = models.CharField(max_length=30, blank=False, null= False)
    slug = AutoSlugField(populate_from='isim', unique=True)

    class Meta:
        db_table='Category'
        verbose_name_plural= 'Categories'
        verbose_name= 'Category'
    def __str__(self):
        return self.isim