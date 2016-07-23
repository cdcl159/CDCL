from django.conf.urls import patterns, url
from cdclSite import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
		url(r'^$', views.index, name = "index"),
		url(r'^about/', views.aboutPage, name = "about"),
		url(r'^constitution/', views.constitutionPage, name = "constitution"),
		url(r'^officers/', views.officersPage, name = "officers"),
		url(r'^clubs/', views.clubsPage, name = "clubs"),
		url(r'^dashboard/$', views.dashboard, name = "dashboard"),
		url(r'^clubManagement/$', views.clubManagement, name = "clubManagement"),
		url(r'^playerManagement/$', views.playerManagement, name = "playerManagement"),
		url(r'^fixtures/$', views.fixtures, name = "fixtures"),
		url(r'^resultsSubmission/$', views.resultsSubmission, name = "resultsSubmission"),
		url(r'^userDetails/$', views.userDetails, name = "userDetails"),
	) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)