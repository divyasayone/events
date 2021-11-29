from django.urls import path,include
from django.conf.urls import url

from core.views import (IndexView,TestView)


urlpatterns	=	[
	# user account management
    url(r'^home/',IndexView.as_view(),name='home'),
    
	url(r'^test/',TestView.as_view(),name='test'),

	]