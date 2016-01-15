# -*- coding: utf-8 -*-

#=============================================================================
# 
# File : feeds.py                                                                         
# Author : Hodonou SOUNTON                            
# Team : drxos, kiah, fall, geolov, sadj
# Site : http://reysh.com                                                       
# Date : 2016-01-14T23:18:12+01:00
# Licence : © Reysh Tech, All Right Reserved.
#                                                                            
#=============================================================================



# Stdlib imports
# ----------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals


# ============================================================================





# Core Django imports
# ----------------------------------------------------------------------------

from django.contrib.syndication.views import Feed
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse


# ============================================================================





# Third-party app imports
# ----------------------------------------------------------------------------



# ============================================================================





# Imports from our apps
# ----------------------------------------------------------------------------

from .models import Post

# ============================================================================


class LastestPost(Feed):
	title = _('DrXos Blog Lastest Post')
	link = "/"

	def items(self):
		return Post.objects.all()

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.btext

	def item_link(self, item):
		return reverse('weblog:detail-post', args=[item.slug])