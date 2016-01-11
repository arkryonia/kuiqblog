# -*- coding: utf-8 -*-

#=============================================================================
# 
# File : forms.py                                                                         
# Author : Hodonou SOUNTON                            
# Team : drxos, kiah, fall, geolov, sadj
# Site : http://reysh.com                                                       
# Date : 2016-01-11T17:21:31+01:00
# Licence : © Reysh Tech, All Right Reserved.
#                                                                            
#=============================================================================



# Stdlib imports
# ----------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals


# ============================================================================





# Core Django imports
# ----------------------------------------------------------------------------
from django import forms
from django.utils.translation import ugettext as _

# ============================================================================





# Third-party app imports
# ----------------------------------------------------------------------------



# ============================================================================





# Imports from our apps
# ----------------------------------------------------------------------------

from .models import Post, Category


# ============================================================================


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name']


class PostForm(forms.ModelForm):
	category = forms.ModelFormChoiceField(queryset=Category.objects.all())
	class Meta:
		model = Post
		fields = ['title', 'category', 'image', 'image_alt', 'is_public', 'content']
