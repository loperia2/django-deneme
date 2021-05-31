from deneme.models.contact import contactModel
from django.contrib import admin
from deneme.models import categoryModel
from deneme.models import articlesModel
from deneme.models import commentModel



admin.site.register(categoryModel)

class articlesAdmin(admin.ModelAdmin):
    search_fields=('title','content') 
    list_display=(
        'title','create_Date','edit_Date','writer'
    )

admin.site.register(articlesModel,articlesAdmin)

class commentAdmin(admin.ModelAdmin):
    list_display=(
        'writer','create_Date','edit_Date'
    )
    search_fields=(
        'writer_username',
    )

admin.site.register(commentModel, commentAdmin)

class contactAdmin(admin.ModelAdmin):
    list_display=(
        'email','create_Date',
    )
    search_fields=(
        'email',
    )

admin.site.register(contactModel, contactAdmin)