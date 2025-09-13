from django.contrib import admin
from .models import Maullido

class MaullidoAdmin(admin.ModelAdmin):
    readonly_fields = ('postDate', )
    list_display = ('postUser', 'body', 'postDate', 'likes', 'dislikes')  # 👈 columnas visibles
    list_filter = ('postDate', 'postUser')  # 👈 filtros a la derecha
    search_fields = ('body', 'postUser__username')  # 👈 buscador
    ordering = ('-postDate',)  # 👈 orden por defecto

# Register your models here.
admin.site.register(Maullido, MaullidoAdmin)