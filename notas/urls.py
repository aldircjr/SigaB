from django.conf.urls import url
from frequencia import views as viewFrequencia
from . import views

urlpatterns = [
            url(r'^notas/$', views.listaMateria, name='listaMateria'),
            url(r'^notas/(?P<pk>\d+)/$', views.listaAluno, name='listaAluno'),
            url(r'^notas/(?P<pkMateria>\d+)/(?P<pkAluno>\d+)/$', views.notas, name='notas'),
         	
            
            #url(r'^frequencia/(?P<pk>\d+)/$', views.frequenciaNew, name='frequenciaNew'),
         	
            ]