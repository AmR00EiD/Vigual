from audioop import avg
from email import feedparser
import email
from multiprocessing import context
from multiprocessing.dummy import current_process
from sre_parse import CATEGORIES
from urllib import request
from django.shortcuts import  get_object_or_404, render, redirect
from django.contrib.auth.models import User , auth
from django.urls import reverse
from accounts.forms import FreelancerForm, UserForm ,MyPasswordChangeForm
from accounts.models import * 
from django.contrib import messages	
from django.contrib.auth.decorators import login_required
from projects.models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Max
from projects.views import Post
from django.db.models import Q
from django.db.models import Avg

def choose(request):
    return render(request , 'accounts/choose.html')

def freelancersignup(request):
        if request.method == 'POST':
            firstname =request.POST.get('firstname')
            lastname =request.POST.get('lastname')
            dob = request.POST.get('date')
            gender = request.POST.get('inlineRadioOptions')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            phone_number = request.POST.get('phone_number')
            nati=request.POST.get('nationality')
            bank =request.POST.get('banckacc')
            user_type = 'freelancer'
            if password==password2:
                if CustomUser.objects.filter(username=firstname).exists():
                    messages.info(request,'الاسم مستخدم')
                    return redirect('accounts:freelancersignup')
                elif CustomUser.objects.filter(email=email).exists():
                    messages.info(request,'يوجد حساب مستخدم')
                    return redirect('accounts:freelancersignup')
                elif CustomUser.objects.filter(phone_number=phone_number).exists():
                    messages.info(request,'هذا الرقم مستخدم')
                    return redirect('accounts:freelancersignup')
                else:	
                    user = CustomUser.objects.create_user(username=email,gender=gender,email=email,password=password,phone_number=phone_number,first_name =firstname,last_name=lastname,dob=dob,nationality=nati,user_type=user_type ,banckacc=bank  )
                    user.save()
                    messages.info(request,'تم انشاء حسابك بنجاح')
                    return redirect('accounts:login')
            else:
                    messages.info(request,'كلمه المرور غير مطابق')	
                    return redirect('accounts:freelancersignup')	
        else:
            return render(request, 'accounts/Freelancer_signup.html')

def clientsignup(request):
    if request.method == 'POST':
        firstname =request.POST.get('firstname')
        lastname =request.POST.get('lastname')
        dob = request.POST.get('date')
        gender = request.POST.get('inlineRadioOptions')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        phone_number = request.POST.get('phone_number')
        nati=request.POST.get('nationality')
        user_type = 'client'
        if password==password2:
            if CustomUser.objects.filter(username=firstname).exists():
                messages.info(request,'الاسم مستخدم')
                return redirect('accounts:clientsignup')
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request,'يوجد حساب مستخدم')
                return redirect('accounts:clientsignup')
            elif CustomUser.objects.filter(phone_number=phone_number).exists():
                messages.info(request,'هذا الرقم مستخدم')
                return redirect('accounts:clientsignup')
            else:	
                user = CustomUser.objects.create_user(username=email,gender=gender,email=email,password=password,phone_number=phone_number,first_name =firstname,last_name=lastname,dob=dob,nationality=nati,user_type=user_type  )
                user.save()
                messages.info(request,'تم انشاء حسابك بنجاح')
                
                return redirect('accounts:login')
        else:
                messages.info(request,'كلمه السري غير مطابق')	
                return redirect('accounts:clientsignup')	
    else:
        return render(request, 'accounts/Client_signup.html')

def login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=name,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/home")
        elif CustomUser.objects.filter(username=name).exists():
            messages.info(request,'كلمه المرور غير صحيحه')
            return redirect('accounts:login')
        elif CustomUser.objects.filter(email=name).exists():
            messages.info(request,'كلمه المرور غير صحيحه')
            return redirect('accounts:login') 
        else:
            messages.info(request,"لا تملك حساب")	
            return redirect('accounts:login')
    else:
  

        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='accounts:login')
def Profilesfreelancer(request):
    profile_det =freelancer.objects.filter(user=request.user)
    project = projects.objects.filter(freelancerr__in=[request.user.freelancer])
    proj = projects.objects.filter(freelancerr__in=[request.user.freelancer]).count()
    fll=Follow.objects.filter(followed=request.user)
    fl2 =Follow.objects.filter(followed_by=request.user)
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
    rat =rateprofile.objects.filter(rated = request.user).aggregate(avg_rating=Avg('rate'))
            

    context = {'pro':profile_det,'p':project,'t':proj,'follow':fll ,'following':fl2 , 'chats1': chat,'rat':rat}
    return render (request,'profiles/Freelancer_Profile.html' , context )

@login_required(login_url='accounts:login')
def Profilesclient(request,):
    fll=Follow.objects.filter(followed=request.user)
    fl2 =Follow.objects.filter(followed_by=request.user)
    client_post = Post.objects.filter(author__user=request.user.id).order_by('-created_on')
    client_postcount = Post.objects.filter(author__user=request.user.id).count()
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
    rat =rateprofile.objects.filter(rated = request.user).aggregate(avg_rating=Avg('rate'))
    context = {'follow':fll ,'following':fl2,'clientpost':client_post,'client_postcount':client_postcount ,'chats1': chat,'rat':rat}
    return render (request,'profiles/Client_Profile.html',context )

@login_required(login_url='accounts:login')
def FreelancerProfileEdit(request):
    profile_det =freelancer.objects.filter(user=request.user)
    profile_de =freelancer.objects.get(user=request.user)
    project = projects.objects.filter(freelancerr__in=[request.user.freelancer])
    proj = projects.objects.filter(freelancerr__in=[request.user.freelancer]).count()
    fll=Follow.objects.filter(followed=request.user)
    fl2 =Follow.objects.filter(followed_by=request.user)
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
    
    if request.method == 'POST':
        userform=UserForm(request.POST,request.FILES,instance=request.user)
        freelancerform=FreelancerForm(request.POST,instance=profile_de)
        if userform.is_valid()and freelancerform.is_valid():
            userform.save()
            freelancerprofile = freelancerform.save(commit=False)
            freelancerprofile.user =request.user
            freelancerprofile.save()
            return redirect(reverse('accounts:freelancerprofile'))

    else:
        userform=UserForm(instance=request.user)
        freelancerform=FreelancerForm(request.POST,instance=profile_de)	




            

    context = {'pro':profile_det,'p':project,'t':proj,'follow':fll ,'following':fl2,'userform':userform,'freelancerform':freelancerform, 'chats1': chat,}





    return render(request ,'accounts/Edit_Profile.html',context)

@login_required(login_url='accounts:login')
def ClientProfileEdit(request,):
    fll=Follow.objects.filter(followed=request.user)
    fl2 =Follow.objects.filter(followed_by=request.user)
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
    client_post = Post.objects.filter(author=request.user.id)
    client_postcount = Post.objects.filter(author=request.user.id).count()
    if request.method == 'POST':
        userform=UserForm(request.POST,request.FILES,instance=request.user)
        
        if userform.is_valid():
            userform.save()


            return redirect(reverse('accounts:clientprofile'))

    else:
        userform=UserForm(instance=request.user)

    context = {'follow':fll ,'following':fl2,'clientpost':client_post,'client_postcount':client_postcount,'userform':userform, 'chats1': chat,}

    return render(request , 'accounts/Edit_ClientProfile.html',context)

@login_required(login_url='accounts:login')
def freelancer_detail(request,slug):
    freelancer_details = get_object_or_404(freelancer, slug=slug)
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
    pro = projects.objects.filter(freelancerr=freelancer_details)
    proje = projects.objects.filter(freelancerr=freelancer_details).count()
    fll=Follow.objects.filter(followed=freelancer_details.user.id)
    fl2 =Follow.objects.filter(followed_by=freelancer_details.user.id)
    following = False
    rat2 =rateprofile.objects.filter(rated = freelancer_details.user).aggregate(avg_rating=Avg('rate'))
    rat =rateprofile.objects.filter(rated = freelancer_details.user , user = request.user ).first()
    
    if request.user.is_authenticated:


        if request.user.id==freelancer_details.user.id:
              return redirect("accounts:freelancerdetail", slug=freelancer_details)
  
        followers = freelancer_details.user.followers.filter(followed_by__id=request.user.id)
        if followers.exists():
            following = True    



     
        
    if request.method == "POST" :
        rate2 =request.POST['rate']
        user2 = request.user
        rated2 = freelancer_details.user
        su = True
        ratings = rateprofile(user=user2,rated=rated2,rate=rate2,submit=su )   
        ratings.save()     
        return redirect("accounts:freelancerdetail", slug) 


    context ={'p':pro,'frde':freelancer_details ,'j':proje,'follow':fll ,'following5':fl2 ,"following": following,  'chats1': chat,'ratee1':rat ,'ratee2':rat2}

    return render(request,'view/UserF.html',context)

@login_required(login_url='accounts:login')
def client_detail(request,slug):
    client_details =get_object_or_404(client,slug=slug)
    chat = chats.objects.filter(members__in=[request.user.id]).annotate(last_message=Max('massage')).order_by('-last_message')
    fll=Follow.objects.filter(followed=client_details.user.id)
    fl2 =Follow.objects.filter(followed_by=client_details.user.id)
    client_posts = Post.objects.filter(author=client_details).order_by('-created_on')
    client_postcount = Post.objects.filter(author=client_details).count()
    rat2 =rateprofile.objects.filter(rated = client_details.user).aggregate(avg_rating=Avg('rate'))
    rat =rateprofile.objects.filter(rated = client_details.user , user = request.user ).first()
    
    following = False

    if request.user.is_authenticated:


        if request.user.id==client_details.user.id:
              return redirect("accounts:clientdetail", slug=client_details)
  
        followers = client_details.user.followers.filter(followed_by__id=request.user.id)
        if followers.exists():
            following = True
    if request.method == "POST" :
        rate2 =request.POST['rate']
        user2 = request.user
        rated2 = client_details.user
        su = True
        ratings = rateprofile(user=user2,rated=rated2,rate=rate2,submit=su )   
        ratings.save()     
        return redirect("accounts:clientdetail", slug)         

    context ={'clde':client_details,'follow':fll ,'following5':fl2,'clientposts':client_posts,'client_postcount':client_postcount,"following": following, 'chats1': chat,'ratee1':rat ,'ratee2':rat2 }




    return render(request,'view/UserC.html',context)




@login_required(login_url='accounts:login')
def follow_or_unfollow_client(request,  slug):
    followed = get_object_or_404(CustomUser, client__slug=slug)
    followed_by = get_object_or_404(CustomUser, id=request.user.id)

    follow, created = Follow.objects.get_or_create(
        followed=followed,
        followed_by=followed_by
    )

    if created:
        followed.followers.add(follow)

    else:
        followed.followers.remove(follow)
        follow.delete()

    return redirect("accounts:clientdetail", slug) 


@login_required(login_url='accounts:login')
def follow_or_unfollow_freelancer(request,  slug):
    followed = get_object_or_404(CustomUser,  freelancer__slug=slug)
    followed_by = get_object_or_404(CustomUser, id=request.user.id)

    follow, created = Follow.objects.get_or_create(
        followed=followed,
        followed_by=followed_by
    )

    if created:
        followed.followers.add(follow)

    else:
        followed.followers.remove(follow)
        follow.delete()

    
    return redirect("accounts:freelancerdetail", slug)       


@login_required(login_url='accounts:login')
def delete(request, id):
    del_proj = get_object_or_404(projects,id=id).delete()
    
    context={}
    return render(request,reverse('profiles/Freelancer_Profile.html'),context)



def rate (request):
    pass    
