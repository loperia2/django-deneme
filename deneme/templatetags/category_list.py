from django import template
from deneme.models import categoryModel

register = template.Library()

@register.simple_tag
def category_list():
    categories = categoryModel.objects.all()
    
    return categories