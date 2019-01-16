from django.conf.urls import url
from . import views

urlpatterns = [
    url('about/', views.about, name = 'about'),
    url('blog/', views.blog, name='blog'),
    url('blog_single/', views.blog_single, name='blog_single'),
    url('contact/', views.contact, name='contact'),
    url('index/', views.index, name='index'),
    url('portfolio/', views.portfolio, name='portfolio'),
    url('services/', views.services, name='services'),
    url('support/', views.support, name='support'),
    url('technology/', views.technology, name='technology'),

]