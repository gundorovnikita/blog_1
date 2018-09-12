from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'posts'

urlpatterns = [

    url(r'^$', views.ListView.as_view(), name='index'), 

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(),  name='detail'),

]
#    url(r'^$', views.ListView.as_view(), name='index'),
