from urllib.parse import quote_plus

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm
from .models import Post
# Create your views here.

#Hay vistas basadas en funciones y otras basadas en clases.
#Usaremos vistas basadas en funciones

#Crear
def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.usuario = request.user
		instance.save()
		#Mensaje de Exito si el formulario es valido
		messages.success(request, "Post Creado Exitosamente!.")
		return HttpResponseRedirect(instance.get_absolute_url())
	contexto = {
		"form": form,
	}
	return render(request, "post_form.html", contexto)

#Detalle
def post_detail(request, slug=None):#Retrieve
	instance = get_object_or_404(Post, slug=slug)
	if instance.borrador or instance.publicar > timezone.now().date():
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.contenido)
	contexto = {
		"titulo": 	instance.titulo,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "post_detail.html", contexto)

#Listar Items
def post_list(request):
	today = timezone.now().date()
	queryset_list = Post.objects.active()#.order_by("-timestamp")#Orden de creacion
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()
	
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(titulo__icontains=query)|
				Q(contenido__icontains=query)|
				Q(usuario__first_name__icontains=query)|
				Q(usuario__last_name__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 2) # Muestra 10 posts por pagina
	page_request_var = "pagina"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	contexto = {
		"object_list": queryset,
		"titulo": "Lista", 
		"page_request_var":page_request_var,
		"today": today,
	}
	return render(request,"post_list.html",contexto)

#Actualizar
def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#Mensaje de Exito si el formulario es valido
		messages.success(request, "Post Actualizado Exitosamente!")
		return HttpResponseRedirect(instance.get_absolute_url())
	contexto = {
		"titulo": 	instance.titulo,
		"instance": instance,
		"form": form,
	}
	return render(request, "post_form.html", contexto)


#Borrar
def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Post Borrado Correctamente!")
	return redirect("posts:list")#list es el name de list en urls.py de apps/posts