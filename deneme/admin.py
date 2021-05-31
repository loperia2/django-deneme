from django.contrib import admin
from deneme.models import categoryModel
from deneme.models import articlesModel

admin.site.register(categoryModel)

class articlesAdmin(admin.ModelAdmin):
    search_fields=('title','content') 
    list_display=(
        'title','create_Date','edit_Date','writer'
    )

admin.site.register(articlesModel,articlesAdmin)
