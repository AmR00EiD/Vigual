from unicodedata import name
from django.urls import include, path
from . import views


urlpatterns = [
       
    path('', views.index, name='index'),
    path('home/',views.home, name='home'),
    path('followhome/',views.followhome, name='followhome'),
    path('contactus/',views.contactus, name='contactus'),
    path('contactuss/',views.contactuss, name='contactuss'), 
    path('about/',views.about, name='about'),
    path('accounts/',include('accounts.urls', namespace='accounts')),
    path('projects/',include('projects.urls')),
    path('cat/<slug:slug>',views.cat_home, name='cat'),
    path('search/',views.search,name='search')
    ]       