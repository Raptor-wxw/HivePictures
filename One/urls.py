from django.conf.urls import url
from One import views

urlpatterns = [
    url(r'^search/(.+)', views.search, name='search'),
    url(r'^picture/(\d+)/', views.picture, name='picture'),
    url(r'^image/', views.image, name='image'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^suggestion', views.suggestion, name='suggestion'),
    url(r'^video/', views.video, name='video'),
    url(r'^show/', views.show, name='show'),
    url(r'^about/', views.about, name='about'),
    url(r'^', views.index, name='index'),
]
