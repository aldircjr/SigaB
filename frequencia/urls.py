from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'^$', views.mainPage, name='mainPage'),
            url(r'^frequencia/$', views.frequencia, name='frequencia'),
            url(r'^frequencia/(?P<pk>\d+)/$', views.frequenciaNew, name='frequenciaNew'),
         	
            ]