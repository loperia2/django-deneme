from enum import unique
from django.db import models
from autoslug import AutoSlugField
from deneme.models import categoryModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from deneme.abstract_models import DateAbstractModel

class articlesModel(DateAbstractModel):
    img= models.ImageField(upload_to='articles_images')
    title = models.CharField(max_length=50)
    content = RichTextField()
    slug = AutoSlugField(populate_from='title', unique=True)
    categories= models.ManyToManyField(categoryModel, related_name='article')
    writer= models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='articles')

    class Meta:
        db_table='Article'
        verbose_name= 'article'
        verbose_name_plural= 'Articles'
    def __str__(self):
        return self.title