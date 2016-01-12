# -*- coding: utf-8 -*-

#=============================================================================
# 
# File : admin.py                                                                         
# Author : Hodonou SOUNTON                            
# Team : drxos, kiah, fall, geolov, sadj
# Site : http://reysh.com                                                       
# Date : 2016-01-07T12:02:38+01:00
# Licence : © Reysh Tech, All Right Reserved.
#                                                                            
#=============================================================================



# Stdlib imports
# ----------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals


# ============================================================================





# Core Django imports
# ----------------------------------------------------------------------------
from django.contrib import admin
from django.contrib.auth.models import Group


# ============================================================================





# Third-party app imports
# ----------------------------------------------------------------------------
from ckeditor.widgets import CKEditorWidget

# ============================================================================





# Imports from our apps
# ----------------------------------------------------------------------------

from .models import Category, Post, Author, Editor
from kuiqblog.users.models import User


# ============================================================================

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	date_hierarchy = 'created'
	exclude = ['author']
	list_display = ('title', 'author', 'created', 'is_public', 'category')	
	prepopulated_fields = {'slug': ('title',)}
	
	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.save()

	def get_queryset(self, request):
		qs = super(PostAdmin, self).get_queryset(request)
		groups = []


		if request.user.is_superuser or request.user.has_perm('users.is_editor'):						
			return qs


		return qs.filter(author=request.user)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):	
	exclude = ['groups', 'has_perms', 'is_superuser', 'is_staff', 'last_login', 'password', 'user_permissions']
	list_display = ('first_name', 'last_name', 'username', 'is_active', 'last_login')	
	
	def save_model(self, request, obj, form, change):
		obj.password = 'pass'	
		obj.is_superuser = False
		obj.is_staff = True
		obj.save()
		obj.groups.add(Group.objects.get(name='author'))


@admin.register(Editor)
class EditorAdmin(admin.ModelAdmin):
	pass