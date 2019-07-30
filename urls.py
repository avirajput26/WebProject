from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('/about',views.about, name='about'),
    path('',views.contact, name='contact'),
    path('',views.destinations, name='destinations'),
    path('',views.elements, name='elements'),
    path('',views.news, name='news'),
]
