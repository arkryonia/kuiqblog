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

from . import views


# ============================================================================


urlpatterns = [


	# Categories URLs
	url(

		regex=r"^backend/categories/$",
		view=views.CategoryBackListView.as_view(),
		name="list-categories"
	),

	url(
		regex=r"^backend/category/create/",
		view=views.CategoryBackCreateView.as_view(),
		name="create-category"
	),

	url(
		regex=r"^backend/categories/(?P<pk>\d+)/$",
		view=views.CategoryBackDetailView.as_view(),
		name='detail-category'
	),

	url(
		regex=r"^backend/category/update/(?P<pk>\d+)/$",
		view=views.CategoryBackUpdateView.as_view(),
		name='update-category'
	),


	# Posts URLs

	url(
		regex=r"^backend/posts/$",
		view=views.PostBackListView.as_view(),
		name="backend-posts-list"
	),	

	url(
		regex=r"^backend/posts/create/$",
		view=views.PostBackCreateView.as_view(),
		name="backend-post-create"
	),

	url(
		regex=r"^backend/posts/(?P<pk>\d+)/$",
		view=views.PostBackDetailView.as_view(),
		name="backend-post-detail"
	),


	url(

		regex=r"^backend/posts/update/(?P<pk>\d+)/$",
		view=views.PostBackUpdateView.as_view(),
		name="backend-post-update"
	),


	# url(
	# 	regex=r"^backend/posts/(?P<pk>\d+)/pub/$",
	# 	view=views.pub_post,
	# 	name="pub-post"
	# ),
	

	# url(
	# 	regex=r"^posts/feeds/$",
	# 	view=feeds.LastestPost(),
	# 	name="feeds"
	# ),




	# url(
	# 	regex=r"^$",
	# 	view=views.PostPublicListView.as_view(),
	# 	name="public-list-posts"
	# ),

	# url(

	# 	regex=r"^(?P<slug>[-\w]+)/$",
	# 	view=views.PostPublicDetailView.as_view(),
	# 	name="public-detail-post"
	# ),

]