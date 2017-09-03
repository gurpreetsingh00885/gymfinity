from django.conf.urls import url, include
from django.contrib import admin

from registration.views import HomeView, AddGymView, FindGymView

urlpatterns = [
	url(r'^accounts/', include('allauth.urls')),
	url(r'^find/', FindGymView.as_view()),
	url(r'^partner/', AddGymView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^/', HomeView.as_view()),
]
