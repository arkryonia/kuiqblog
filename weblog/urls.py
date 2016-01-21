# -*- coding: utf-8 -*-

#=============================================================================
# 
# File : urls.py                                                                         
# Author : Hodonou SOUNTON                            
# Team : drxos, kiah, fall, geolov, sadj
# Site : http://reysh.com                                                       
# Date : 2016-01-11T17:52:42+01:00
# Licence : © Reysh Tech, All Right Reserved.
#                                                                            
#=============================================================================



# Stdlib imports
# ----------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals


# ============================================================================





# Core Django imports
# ----------------------------------------------------------------------------
from django.conf.urls import url



# ============================================================================





# Third-party app imports
# ----------------------------------------------------------------------------



# ============================================================================





# Imports from our apps
# ----------------------------------------------------------------------------

from . import views, feeds


# ============================================================================


urlpatterns = [

	url(
		regex=r"^$",
		view=views.PostListView.as_view(),
		name="list-posts"
	),

	url(
		regex=r"^(?P<slug>[\w-]+)/$",
		view=views.PostListbyCategoryView.as_view(),
		name="list-category-posts"
	),


	url(
		regex=r"^posts/(?P<slug>[\w-]+)/$",
		view=views.PostDetailView.as_view(),
		name="detail-post"
	),
	
	url(
		regex=r"^posts/feeds/$",
		view=feeds.LastestPost(),
		name="feeds"
	),
]