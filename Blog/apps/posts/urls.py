from django.conf.urls import url
from django.contrib import admin
from apps.posts import views as post_view

urlpatterns = [
	#url(r'^$', post_view.post_home),
	url(r'^$',   post_view.post_list, name='list'),#HomePage para posts
	url(r'^create/$', post_view.post_create),
	url(r'^(?P<slug>[\w-]+)/$', post_view.post_detail, name='detail'),
	url(r'^(?P<slug>[\w-]+)/edit/$', post_view.post_update, name='update'),
	url(r'^(?P<slug>[\w-]+)/delete/$', post_view.post_delete),
]