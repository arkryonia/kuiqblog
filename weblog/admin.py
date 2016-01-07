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



# ============================================================================





# Third-party app imports
# ----------------------------------------------------------------------------



# ============================================================================





# Imports from our apps
# ----------------------------------------------------------------------------
from .models import Category, Post



# ============================================================================

class PostAdmin(admin.ModelAdmin):
	exclude = ['author']
	prepopulated_fields = {'slug': ('title',)}


	def save_model(sself, request, obj, form, change):
		obj.author = request.user
		obj.save()


class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}




admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)