from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from accounts.models import CustomUser, Follow, chats, rateprofile
from projects.models import *
from django.db.models import Q
from django.db.models import Max
from django.db.models import Avg
from accounts.models import contuctus
from django.contrib import messages

def index(request):
        
        
        if request.user.is_authenticated:
                if request.method =="POST":
                        user =request.user
                        email =request.user.email
                        subject =request.POST.get('subject')
                        message =request.POST.get('message')    
                        contact = contuctus(user=user,email=email,title=subject,content=message)
                        contact.save()
                        messages.success(request, 'شكرا لتواصلك معنا')               
                        return HttpResponseRedirect(reverse("index")) 
               
               
        else :       
                if request.method =="POST":
                        user =request.POST.get('name')
                        email =request.POST.get('email')
                        subject =request.POST.get('subject')
                        message =request.POST.get('message')
                        if CustomUser.objects.filter(email=email).exists():
                                messages.success(request, 'هذا البريد مستخدم بالفعل') 
                                return redirect('contactuss')
                        else :            
                                contact = contuctus(outside_user=user,email=email,title=subject,content=message)
                                contact.save()
                                messages.success(request, 'شكرا لتواصلك معنا') 
                        return HttpResponseRedirect(reverse("index"))       

                

        
        return render(request,'home/index.html')

def contactus(request):
        chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
        if request.user.is_authenticated:
                if request.method =="POST":
                        user =request.user
                        email =request.user.email
                        subject =request.POST.get('subject')
                        message =request.POST.get('message')    
                        contact = contuctus(user=user,email=email,title=subject,content=message)
                        contact.save()
                        messages.success(request, 'شكرا لتواصلك معنا')               
                        return HttpResponseRedirect(reverse("contactus")) 
               
               
        else :       
                if request.method =="POST":
                        user =request.POST.get('name')
                        email =request.POST.get('email')
                        subject =request.POST.get('subject')
                        message =request.POST.get('message')
                        if CustomUser.objects.filter(email=email).exists():
                                messages.success(request, 'هذا البريد مستخدم بالفعل') 
                                return redirect('contactuss')
                        else :            
                                contact = contuctus(outside_user=user,email=email,title=subject,content=message)
                                contact.save()
                                messages.success(request, 'شكرا لتواصلك معنا') 
                        return HttpResponseRedirect(reverse("contactus"))     
                          

        
        
        
        
        
        
        return render(request,'home/contactUs.html', {'chats1': chat})

def contactuss(request):
        chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
        if request.user.is_authenticated:
                if request.method =="POST":
                        user =request.user
                        email =request.user.email
                        subject =request.POST.get('subject')
                        message =request.POST.get('message')    
                        contact = contuctus(user=user,email=email,title=subject,content=message)
                        contact.save()
                        messages.success(request, 'شكرا لتواصلك معنا')               
                        return HttpResponseRedirect(reverse("contactus")) 
               
               
        else :       
                if request.method =="POST":
                        user =request.POST.get('name')
                        email =request.POST.get('email')
                        subject =request.POST.get('subject')
                        message =request.POST.get('message')
                        if CustomUser.objects.filter(email=email).exists():
                                messages.success(request, 'هذا البريد مستخدم بالفعل') 
                                return redirect('contactuss')
                        else :            
                                contact = contuctus(outside_user=user,email=email,title=subject,content=message)
                                contact.save()
                                messages.success(request, 'شكرا لتواصلك معنا') 
                        return HttpResponseRedirect(reverse("contactus"))     
                          

        
        
        
        
        
        
        return render(request,'home/contactUss.html', {'chats1': chat})




def about(request):
        chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
        if request.user.is_authenticated:
                if request.method =="POST":
                        user =request.user
                        email =request.user.email
                        subject =request.POST.get('subject')
                        message =request.POST.get('message')    
                        contact = contuctus(user=user,email=email,title=subject,content=message)
                        contact.save()
                        messages.success(request, 'شكرا لتواصلك معنا')               
                        return HttpResponseRedirect(reverse("about")) 
               
               
        else :       
                if request.method =="POST":
                        user =request.POST.get('name')
                        email =request.POST.get('email')
                        subject =request.POST.get('subject')
                        message =request.POST.get('message')
                        if CustomUser.objects.filter(email=email).exists():
                                messages.success(request, 'هذا البريد مستخدم بالفعل') 
                                return redirect('contactuss')
                        else :            
                                contact = contuctus(outside_user=user,email=email,title=subject,content=message)
                                contact.save()
                                messages.success(request, 'شكرا لتواصلك معنا') 
                        return HttpResponseRedirect(reverse("about"))    
        return render(request,'home/about.html', {'chats1': chat})        

def home(request,):
       chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')

       project1=projects.objects.all().order_by('-created_on')
       
       rat =rateprofile.objects.filter().aggregate(avg_rating=Avg('rate'))
       context={
               'pro88':project1, 'chats1': chat,'rat':rat,}

       return render (request=request,template_name= 'home/home.html',context=context)

def followhome(request,):
       chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
       project1=projects.objects.filter(freelancerr__user__followers__followed_by=request.user.id ).order_by('-created_on')
       
       rat =rateprofile.objects.filter().aggregate(avg_rating=Avg('rate'))
       context={
               'pro88':project1, 'chats1': chat,'rat':rat,}

       return render (request=request,template_name= 'home/followhome.html',context=context)       
        

def cat_home (request,slug):
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')    
    sidcat =get_object_or_404(Category,slug=slug)
    project1=projects.objects.filter(cat=sidcat)



    context ={'sidcat':sidcat,'pro88':project1, 'chats1': chat,}

    return render(request=request,template_name='home/cat.html',context=context) 


def search(request):
       chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
       project1=projects.objects.all().order_by('-created_on')
       users=CustomUser.objects.all()
       name =None
       proname =None
       if 'searchname' in request.GET:
                name = request.GET['searchname']
                if name:
                        project1 = project1.filter(Q(freelancerr__user__first_name__icontains=name)|Q(freelancerr__user__last_name__icontains=name)|Q(Name__icontains=name))
                        allusers = users.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
       
       
       
       context={
               'pro88':project1,'name':name, 'chats1': chat,'allusers':allusers}
       return render (request=request,template_name= 'home/search.html',context=context)


      
       



