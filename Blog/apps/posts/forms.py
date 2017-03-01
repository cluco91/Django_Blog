from django import forms
from .models import Post

#Clase de Formulario, forms extiende de ModelForm
class PostForm(forms.ModelForm):
	class Meta:
		#Modelo
		model = Post
		#Campos
		fields = [
		#Aqui defino el orden del formulario
			"titulo",
			"contenido",
			"imagen",
			"borrador",
			"publicar",
		]