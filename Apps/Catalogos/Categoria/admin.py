from django.contrib import admin
from Apps.Catalogos.Categoria.models import Categoria

# Register your models here.
@admin.register(Categoria)

class ArticleAdmin(admin.ModelAdmin):
     list_display = ['Codigo', 'Nombre']
     search_fields = ['Codigo', 'Nombre']
