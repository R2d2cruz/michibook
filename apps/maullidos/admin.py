from django.contrib import admin
from .models import Maullido, MaullidoReaction

class MaullidoAdmin(admin.ModelAdmin):
    readonly_fields = ('postDate', )
    list_display = ('postUser', 'body', 'postDate')  # 👈 columnas visibles
    list_filter = ('postDate', 'postUser')  # 👈 filtros a la derecha
    search_fields = ('body', 'postUser__username')  # 👈 buscador
    ordering = ('-postDate',)  # 👈 orden por defecto

class MaullidoReactionAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'maullido')
    list_display = ('user', 'maullido', 'reaction')  # 👈 columnas visibles
    list_filter = ('user', 'maullido', 'reaction')  # 👈 filtros a la derecha
    search_fields = ('user', 'maullido', 'reaction')  # 👈 buscador
    ordering = ('maullido',)  # 👈 orden por defecto

# Register your models here.
admin.site.register(Maullido, MaullidoAdmin)
admin.site.register(MaullidoReaction, MaullidoReactionAdmin)