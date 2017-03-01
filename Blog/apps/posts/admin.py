from django.contrib import admin

# Register your models here.
#Uso .models porque esta en la misma carpeta posts
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	#Esto lo veremos en /admin/posts donde se listan los post
	#TITULO - UPDATED - TIMESTAMP, ANTES SOLO SE MOSTRABA TITULO
	list_display = ["titulo", "updated","timestamp"]
	list_display_links = ["updated"]#Muestra los UPDATED como vinculos
	list_editable = ["titulo"]#Con esto puedo editar el titulo del post en el listado directamente
	list_filter = ["updated", "timestamp"]#Muestra un sidebar con funcion de filtrado
	search_fields = ["titulo","contenido"]#Barra busqueda para buscar por titulo o contenido
	class Meta:
		model = Post

#De esta forma conectamos el modelo Post con el modelo PostModelAdminPostModelAdmin
admin.site.register(Post, PostModelAdmin)