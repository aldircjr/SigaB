from django.conf.urls import url
from frequencia import views as viewFrequencia
from . import views

urlpatterns = [
            url(r'^notas/$', views.notas, name='notas'),
            #url(r'^frequencia/(?P<pk>\d+)/$', views.frequenciaNew, name='frequenciaNew'),
         	
            ]