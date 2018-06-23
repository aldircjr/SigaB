from django.conf.urls import url, include
from . import views

urlpatterns = [
            url(r'^$', views.mainPage, name='mainPage'),
            #url(r'^frequencia/$', views.frequencia, name='frequencia'),
            #url(r'^frequencia/(?P<pk>\d+)/$', views.frequenciaNew, name='frequenciaNew'),
            url(r'^notas/$', views.listaMateria, name='listaMateria'),
            url(r'^notas/(?P<pk>\d+)/$', views.listaAluno, name='listaAluno'),
            url(r'^notas/(?P<pkMateria>\d+)/(?P<pkAluno>\d+)/$', views.notas, name='notas'),
            url(r'^novoaluno/$', views.novoaluno, name='novoaluno'),
            url(r'^novamateria/$', views.novamateria, name='novamateria'),
            url(r'^listaralunos/$', views.listaralunos, name='listaralunos'),
            url(r'', include('blog.urls')),
            ]