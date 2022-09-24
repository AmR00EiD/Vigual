
from tempfile import template
from typing_extensions import Self
from django.urls import include, path, reverse_lazy
from . import views
from django.contrib.auth.views import PasswordChangeView ,PasswordChangeDoneView
from .forms import MyPasswordChangeForm

app_name= 'accounts'

urlpatterns = [
       
    path('',views.login, name='login'),
    path('login',views.login, name='login'),
    path('freelancersignup',views.freelancersignup, name='freelancersignup'),
    path('clientsignup',views.clientsignup, name='clientsignup'),
    path('logout',views.logout, name='logout'),
    path('choose',views.choose, name='choose'),
    path('freelancer/',views.Profilesfreelancer, name='freelancerprofile'),
    path('client/',views.Profilesclient, name='clientprofile'),
    path('orders',include('projects.urls')),
    path('editfreelancer',views.FreelancerProfileEdit,name= 'editfreelancer'),
    path('editclient',views.ClientProfileEdit,name='editclient'),
    path('freelancer/<slug:slug>/',views.freelancer_detail,name='freelancerdetail'),
    path('client/<slug:slug>/',views.client_detail,name='clientdetail'),
    path('change_password/',PasswordChangeView.as_view(template_name='accounts\changepassword.html',success_url=reverse_lazy('accounts:login'),form_class=MyPasswordChangeForm),name='password_change'),
    path('follow_or_unfollow_user/<slug:slug>/', views.follow_or_unfollow_client, name='follow_or_unfollow_user'),
    path('follow_or_unfollow_freelancer/<slug:slug>/', views.follow_or_unfollow_freelancer, name='follow_or_unfollow_freelancer'),
    path('delete/<int:id>/',views.delete,name='deleteprojects')





    ] 