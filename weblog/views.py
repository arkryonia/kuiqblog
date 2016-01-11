# -*- coding: utf-8 -*-

#=============================================================================
# 
# File : views.py                                                                         
# Author : Hodonou SOUNTON                            
# Team : drxos, kiah, fall, geolov, sadj
# Site : http://reysh.com                                                       
# Date : 2016-01-11T17:14:24+01:00
# Licence : © Reysh Tech, All Right Reserved.
#                                                                            
#=============================================================================



# Stdlib imports
# ----------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals


# ============================================================================





# Core Django imports
# ----------------------------------------------------------------------------

from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.utils.text import slugify


# ============================================================================





# Third-party app imports
# ----------------------------------------------------------------------------

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

# ============================================================================





# Imports from our apps
# ----------------------------------------------------------------------------

from .models import Category, Post
from .forms import PostForm, CategoryForm


# ============================================================================


# Categry Views >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class CategoryCreateView(
			LoginRequiredMixin, 
			PermissionRequiredMixin,
			CreateView):
	"""
		This class allows admin users to create categories
	"""
	model = Category
	form_class = CategoryForm
	success_url = reverse_lazy('weblog:list-cats')
	template_name = ''
	permission_required = 'auth.is_editor'
	raise_exception = True
	
	
	def dispatch(self, *args, **kwargs):
		return super(CategoryCreateView, self).dispatch(*args, **kwargs)


class CategoryListView(
			LoginRequiredMixin, 
			PermissionRequiredMixin,
			ListView):
	"""
		This class aims to list categories.
	"""
	model = Category
	template_name = ''
	context_object_name = 'categories'
	permission_required = 'auth.is_editor'
	raise_exception = True

	

class CategoryDetailView(
			LoginRequiredMixin, 
			PermissionRequiredMixin,
			DetailView):
	"""
		This class allows to detail a category object.
	"""
	model = Category
	permission_required = 'auth.is_editor'
	raise_exception = True

	

class CategoryUpdateView(
			LoginRequiredMixin, 
			PermissionRequiredMixin,
			UpdateView):
	"""
		This class aims to update a category object
	"""
	model = Category
	fields = ['name']
	success_url = reverse_lazy('weblog:list-cats')
	template_name = ''
	permission_required = 'auth.is_editor'
	raise_exception = True

# End category views <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<




# Post views >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class PostBackCreateView(
			LoginRequiredMixin, 
			PermissionRequiredMixin,
			CreateView):
	"""
		This class allows admin users to create categories
	"""
	model = Post
	form_class = PostForm	
	success_url = reverse_lazy('weblog:list-posts')
	template_name = 'weblog/backend/posts/create.html'
	permission_required = 'auth.is_author'
	raise_exception = True

	
	def form_valid(self, form):	
		form.instance.author = self.request.user
		return super(PostBackCreateView, self).form_valid(form)


class PostBackListView(
			LoginRequiredMixin, 
			PermissionRequiredMixin,
			ListView):
	"""
		This class aims to list categories.
	"""
	model = Post
	paginate_by = 2
	template_name = 'weblog/backend/posts/list.html'
	context_object_name = 'posts'
	permission_required = 'auth.is_author'
	raise_exception = True

	
	def get_queryset(self):		
		user = self.request.user
		queryset = user.post_set.all()
		return queryset

class PostDetailView(
			LoginRequiredMixin, 
			PermissionRequiredMixin,
			DetailView):
	"""
		This class aims to list categories.
	"""
	model = Post
	template_name = 'weblog/backend/posts/detail.html'
	context_object_name = 'post'
	permission_required = 'auth.is_author'
	raise_exception = True



class PostBackUpdateView(
			LoginRequiredMixin, 
			PermissionRequiredMixin,
			UpdateView):
	"""
		This class aims to update a category object
	"""
	model = Post
	fields = ['title', 'category', 'image', 'image_alt', 'is_public', 'content']
	success_url = reverse_lazy('weblog:list-posts')
	template_name = 'weblog/backend/posts/create.html'
	permission_required = 'auth.is_author'
	raise_exception = True


# End Post views <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<