from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.db.models import Count
from accounts.forms import massagesform
from accounts.models import Massage, chats, client
from projects.models import Post , Comment
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q
from django.db.models import Max
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

@login_required(login_url='accounts:login')
@user_passes_test(lambda user: user.user_type == 'client', login_url='ac')
def Estlam(request):
    forms = orderprocssing.objects.filter(receiver__in=[request.user.client]).order_by('-created_on')
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
    context ={'forms':forms ,'chats1': chat,}
    return render(request,'orders/Estlam.html',context)

@login_required(login_url='accounts:login')
@user_passes_test(lambda user: user.user_type == 'freelancer', login_url='ac')
def Taslem(request):
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
    if request.method =='POST':
        
        add_Project= ProjectsForm(request.POST,request.FILES,)
     
        if add_Project.is_valid():
            pr=add_Project.save(commit=False)
            pr.freelancerr = request.user.freelancer
            pr.save() 
            return HttpResponseRedirect(reverse("accounts:freelancerprofile"))  



    return render(request,'orders/Taslem.html',{'Form':ProjectsForm(),'chats1': chat,})  

@login_required(login_url='accounts:login')
@user_passes_test(lambda user: user.user_type == 'freelancer', login_url='ac')
def Taslem2(request):
    forms = orderprocssing.objects.filter(sender__in=[request.user.freelancer]).order_by('-created_on')
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
    return render(request,'orders/allforms.html',{'forms':forms,'chats1': chat,})  


@login_required(login_url='accounts:login')
@user_passes_test(lambda user: user.user_type == 'freelancer', login_url='ac')
def taslemorders(request,order_id):
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
    if request.method =='POST':
        add_order =finalorders(request.POST,request.FILES,user=request.user,pay=True,done=False,pk=order_id)

        if add_order.is_valid():
            p2=add_order.save(commit=False)
            p2.save() 
            o = get_object_or_404(orderprocssing,pk=p2.order.id)
            o.submit=True
            o.save()



            return HttpResponseRedirect(reverse("accounts:freelancerprofile")) 

    
    return render(request,'orders/Taslemorders.html',{'formorders':finalorders(user=request.user,pay=True,done=False,pk=order_id),'chats1': chat,})  








@login_required(login_url='accounts:login')
def post(request,):
    post = Post.objects.all().order_by('-created_on')
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
    
    if request.method =='POST':
        add_Post= PostForm(request.POST,)
        if add_Post.is_valid():
            pr=add_Post.save(commit=False)
            pr.author = request.user.client
            pr.save() 
            return HttpResponseRedirect(reverse("post"))  
    
    context ={'posts':post,'Form':PostForm(),'chats1': chat,}
    return render(request=request,template_name='post/posts.html',context=context)  

@login_required(login_url='accounts:login')
def post_det(request,post_id):
    posts =get_object_or_404(Post,pk=post_id)
    comments = Comment.objects.filter(post=posts)
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
    if request.method =='POST':
       add_comm= commentsform(request.POST,)
       if add_comm.is_valid():
            co=add_comm.save(commit=False)
            co.usercomment = request.user.freelancer
            co.post = posts
            co.save() 
            return HttpResponseRedirect(reverse("post_det" , kwargs={'post_id': post_id}))
    context ={  
        'post':posts,
        'comments':comments,
        'commentform': commentsform()
        ,'chats1': chat,
    }
    return render(request=request,template_name='post/posts_destails.html',context=context)     





def project_det(request,project_id): 
    project =get_object_or_404(projects,pk=project_id)
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
    context ={
        'project':project,
        'chats1': chat,
        


    }
    return render(request,'home/details.html',context) 


@login_required(login_url='accounts:login')

def delete (request,id):
    project_delete = projects.objects.get(id=id)
    project_delete.delete()
    return redirect('accounts:freelancerprofile')



@login_required(login_url='accounts:login')
def orderform (request):
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
    
    if request.method =='POST':
        add_form= orderprocssingform(request.POST,request.FILES,)
        if add_form.is_valid():
            formorder=add_form.save(commit=False)
            formorder.sender = request.user.freelancer
            formorder.save() 
            return HttpResponseRedirect(reverse("taslem2"))  
    
    context ={'orderform':orderprocssingform() ,'chats1': chat,}


    return render(request,'orders/form.html',context)  


@login_required(login_url='accounts:login')
def viewform(request,form_id):
    client_forms = get_object_or_404(orderprocssing,pk=form_id)
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
    downloadorder = get_object_or_404(FinelOrder , order=client_forms)
    if client_forms.sender.user == request.user or client_forms.receiver.user == request.user :    
        if request.method == 'POST' :
            
                    client_forms.confirm = True
                    client_forms.save()        

                    return HttpResponseRedirect(reverse("viewform" , kwargs={'form_id': form_id}))   


        context ={'client_form':client_forms,'download':downloadorder, 'chats1': chat,}

        return render(request,'orders/viewform.html',context)   
    else :
        return redirect(reverse('ac'))   


@login_required(login_url='accounts:login')
def viewform2(request,form_id):
    client_forms = get_object_or_404(orderprocssing,pk=form_id)
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
    if client_forms.sender.user == request.user or client_forms.receiver.user == request.user : 
        context ={'client_form':client_forms, 'chats1': chat,}

        return render(request,'orders/viewform.html',context)  
    else :
        return redirect(reverse('ac')) 

@login_required(login_url='accounts:login')
def deleteform (request,form_id):
    form_delete = orderprocssing.objects.get(id=form_id)
    form_delete.delete()
    return redirect('home')    

""" def firstmessage(request , user_id):
    user =get_object_or_404(CustomUser,pk=user_id)




    return render(request,'orders/firstmessage.html',{'massageform':massagesform()}) 


def chat (request,chat_id,user_id):
    chat = get_object_or_404(chats,pk=chat_id)
    Massages= Massage.objects.filter(Q(chat=chat)|Q(sender=request.user))
    user =get_object_or_404(CustomUser,pk=user_id)
    

    if request.method =='POST':
        mess= massagesform(request.POST)
        if mess.is_valid():
            messa=mess.save(commit=False)
            messa.chat = chat
            messa.reciever = user
            messa.sender = request.user

            messa.save() 
            return HttpResponseRedirect(reverse("chat" , kwargs={'chat_id': chat_id}))  
    context={'chats':chat,'massage':Massages, 'massageform':massagesform() }
    return render(request,'orders/chat.html',context)  """

@login_required(login_url='accounts:login')
def MessagesView( request, chat_id):
        chat = get_object_or_404(chats,pk=chat_id)
        Massages= Massage.objects.filter(Q(chat=chat))
        chat2 = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
        mess = massagesform(request.POST)    
        if request.user in chat.members.all() :
            try:
                chat = chats.objects.get(id=chat_id)
                if request.user in chat.members.all():
                    chat.massage_set.filter(is_readed=False).exclude(author=request.user,chat=chat).update(is_readed=True)
                else:
                    chat = None
            except chats.DoesNotExist:
                chat = None
            
            
    
            if mess.is_valid():
                mess = mess.save(commit=False)
                mess.chat_id = chat_id
                mess.author = request.user
                mess.save()
                return redirect(reverse('messages', kwargs={'chat_id': chat_id})) 

            context={'chats':chat,'massageform':massagesform(),'massage':Massages, 'chats1': chat2, }
            
            return render(request,'orders/chat.html',context) 
        else :
            return redirect(reverse('ac'))   


@login_required(login_url='accounts:login')
def createchat(request, user_id):
        chat = chats.objects.filter(members__in=[request.user.id, user_id]).annotate(c=Count('members')).filter(c=2)
        
        if chat.count() == 0:
            createchats = chats.objects.create()
            createchats.members.add(request.user)
            createchats.members.add(user_id)
        else:
            createchats = chat.first()
        return redirect(reverse('messages', kwargs={'chat_id': createchats.id}))  



@login_required(login_url='accounts:login')
def chatview(request):
        chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
        
        return render(request, 'orders/allmsg.html', {'user_profile': request.user, 'chats1': chat,})


""" class chatview(View):

    
    
    
    
    def get(self, request):
        chat = chats.objects.filter(members__in=[request.user.id])
        mess = Massage.objects.filter(chat=chat)
        return render(request, 'orders/allmsg.html', {'user_profile': request.user, 'chats1': chat,'mess':mess}) """






@login_required(login_url='accounts:login')
def payment(request,order_id):
    payments = get_object_or_404(orderprocssing,pk=order_id)
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
    if request.method == 'POST' :
        
        
        card = request.POST['card']
        exp = request.POST['Expiry1']
        cvc =request.POST['cvc']
        paymentss = Payment(ord_det = payments ,card_number=card,expire=exp,security_code=cvc)
        paymentss.save()
        payments.paid = True
        payments.save()

        
        return HttpResponseRedirect(reverse("viewform2" , kwargs={'form_id': order_id}))





         
    else:
        return render(request,'orders/payment.html',{'pay':payments, 'chats1': chat,})              



def download(request,order_id):
    pass

def ac (request):
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
    context ={'chats1': chat,}
    return render(request,'home/ac.html',context)

      