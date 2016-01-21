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
from django.shortcuts import get_object_or_404


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

def home(request):
	return render(request, 'weblog/frontend/posts.html')


# Post views >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class PostListView(ListView):
	"""
		This class aims to list categories.
	"""
	model = Post
	paginate_by = 3
	template_name = 'weblog/frontend/posts.html'
	context_object_name = 'posts'
	queryset = Post.objects.filter(is_public=True).order_by('-created')


class PostListbyCategoryView(ListView):
	"""
		This class aims to list categories.
	"""
	model = Post
	paginate_by = 3
	template_name = 'weblog/frontend/posts.html'
	context_object_name = 'posts'	
	# queryset = Post.objects.filter(slug=self.kwargs['slug']).order_by('-created')

	def get_queryset(self):
		category = Category.objects.get(slug=self.kwargs['slug'])
		return Post.objects.filter(category=category).order_by('-created')




class PostDetailView(DetailView):
	"""
		This class aims to list categories.
	"""
	model = Post
	template_name = 'weblog/frontend/detail.html'
	context_object_name = 'post'
	query_pk_and_slug = True
	