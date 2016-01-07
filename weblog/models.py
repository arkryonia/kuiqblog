# -*- coding: utf-8 -*-

#=============================================================================
# 
# File : models.py                                                                         
# Author : Hodonou SOUNTON                            
# Team : drxos, kiah, fall, geolov, sadj
# Site : http://reysh.com                                                       
# Date : 2016-01-07T10:17:11+01:00
# Licence : © Reysh Tech, All Right Reserved.
#                                                                            
#=============================================================================



# Stdlib imports
# ----------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals


# ============================================================================





# Core Django imports
# ----------------------------------------------------------------------------

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings

# ============================================================================





# Third-party app imports
# ----------------------------------------------------------------------------



# ============================================================================





# Imports from our apps
# ----------------------------------------------------------------------------

from kuiqblog.contrib.models import TimeStampedModel
from kuiqblog.users.models import User


# ============================================================================


@python_2_unicode_compatible
class Category(TimeStampedModel):
	"""
		Class Category is a TimeStampedModel with the following attributes :
			- title
			- slug
	"""
	name = models.CharField(_('Title'), max_length=50)
	slug = models.SlugField(_('Slug'))

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name 		=_('Category')
		verbose_name_plural = _('Categories')
		ordering 			= ['name']


@python_2_unicode_compatible
class Post(TimeStampedModel):
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	category = models.ForeignKey(Category)
	title = models.CharField(_('Title'), max_length=100)
	slug = models.SlugField(_('Slug'), unique=True)	
	content = models.TextField(_('Content'))
	image = models.ImageField(_('Illustration'), upload_to='images')
	image_alt = models.CharField(_('Image Alt'), max_length=100)	
	public = models.BooleanField(default=False)
		
	
	class Meta:
		verbose_name 		=_('Post')
		verbose_name_plural = _('Posts')
		ordering = ['-created']

	def __str__(self):
		return self.title

	def publish(self):
		self.created = timezone.now()
		self.public = True
		self.save()

	def save(self, *args, **kwargs):
		now = datetime.date.today()			
		self.slug = slugify("%s %s"%(self.title, now))
		super(Post, self).save(*args, **kwargs)

