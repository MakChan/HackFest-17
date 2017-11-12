from django.conf.urls import url

from . import views

app_name = 'org'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^cases/',views.cases, name='cases'),
    url(r'^blog/',views.blog, name='blog'),

]
