from os import name
from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
       
    path('taslem',views.Taslem, name='taslem'),
    path('post',views.post, name='post'),
    path('post_det/<int:post_id>',views.post_det, name='post_det'),
    path('project_det/<int:project_id>',views.project_det, name='project_det'),    
    path('delete/<int:id>',views.delete ,name="delete_pro"),
    path('form/',views.orderform,name='orderform'),
    path('viewform/<int:form_id>',views.viewform,name='viewform'),
    path('deleteform/<int:form_id>',views.deleteform ,name='delete_form'),
    path('createchat/<int:user_id>',views.createchat,name='createchat'),
    path('chat/<int:chat_id>',views.MessagesView, name='messages'),
    path('payment/<int:order_id>',views.payment, name='payment'),
    path('download/<int:order_id>',views.download, name='download'),
    path('chats/',views.chatview , name='chats'),
    path('estlam',views.Estlam, name='estalm'),
    path('viewform2/<int:form_id>',views.viewform2,name='viewform2'),
    path('taslem2',views.Taslem2, name='taslem2'),
    path('taslemorders/<int:order_id>',views.taslemorders, name='taslemorders'),
    path('ac',views.ac, name='ac'),
    ]

