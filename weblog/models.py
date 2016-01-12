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
import datetime


# ============================================================================





# Core Django imports
# ----------------------------------------------------------------------------

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings
from django.db.models import permalink

# ============================================================================





# Third-party app imports
# ----------------------------------------------------------------------------

from ckeditor.fields import RichTextField


# ============================================================================





# Imports from our apps
# ----------------------------------------------------------------------------

from kuiqblog.contrib.models import TimeStampedModel
from kuiqblog.users.models import User


# ============================================================================

@python_2_unicode_compatible
class Author(User):
	avatar = models.ImageField(_('Illustration'), upload_to='images', blank=True)
	class Meta:
		verbose_name 		=_('Author')
		verbose_name_plural = _('Authors')

@python_2_unicode_compatible
class Editor(Author):
	class Meta:
		verbose_name 		=_('Editor')
		verbose_name_plural = _('Editors')


@python_2_unicode_compatible
class Category(TimeStampedModel):
	"""
		Class Category is a TimeStampedModel with the following attributes :
			- title
			- slug
	"""
	name = models.CharField(_('Title'), max_length=50, db_index=True)
	slug = models.SlugField(_('Slug'), max_length=50, db_index=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	@permalink
	def get_absolute_url(self):
		from django.core.urlresolvers import reverse
		return reverse('category_details', args=[str(self.slug)])

	def __str__(self):
		return self.name

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
	content = RichTextField(_('Content'))
	image = models.ImageField(_('Illustration'), upload_to='images', blank=True)
	image_alt = models.CharField(_('Image Alt'), max_length=100, blank=True)	
	is_public = models.BooleanField(default=False)

	@permalink
	def get_absolute_url(self):
		from django.core.urlresolvers import reverse
		return reverse('post_details', args=[self.slug])

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

	class Meta:
		verbose_name 		=_('Post')
		verbose_name_plural = _('Posts')
		ordering = ['-created']

