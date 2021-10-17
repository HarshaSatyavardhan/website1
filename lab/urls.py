
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('index', views.homepage, name='homepage'),
    path('publications', views.publications, name='publications'),

    path('alumni', views.alumni, name='alumni'),

    path('contact', views.contact, name='contact'),
    path('joinus', views.positionsjoin, name='joinus'),
    path('phd_students', views.phdstudents, name='phdstudents'),
    path('pi', views.pi, name='pi'),

    path('project1', views.project1, name='project1'),
    path('result', views.result, name='result'),
    
    path('research', views.research, name='research'),
    path('researchers',views.researchers, name='researchers'),
    path('shiladit', views.shiladit, name='shiladit'),
    path('students', views.students, name='students'),
    path('team', views.students, name='team'),



] 
