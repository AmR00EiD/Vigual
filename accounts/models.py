from ast import mod
from email.message import Message
from typing_extensions import Self
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    nationalityx=[
                    ('مصري','مصري'),('صومالي','صومالي'),('اردني','اردني'),
                    ('ليبي','ليبي'),('جيبوتي','جيبوتي'),('قطري','قطري'),
                    ('سوداني','سوداني'),('سوري','سوري'),('اماراتي','اماراتي'),
                    ('جزائري','جزائري'),('فلسطيني','فلسطيني'),('بحرني','بحرني'),
                    ('مغربي','مغربي'),('لبناني','لبناني'),('عماني','عماني'),
                    ('موريتاني','موريتاني'),('عراقي','عراقي'),('يمني','يمني'),
                    ('تونسي','تونسي'),('كويتي','كويتي'),('سعودي','سعودي'),]    
    genderx=[('male','male'),('female','female') ]
    gender = models.CharField( choices=genderx, max_length=15, blank=True ,null=False)
    phone_number= models.IntegerField( blank=True ,null=True)
    nationality=models.TextField(null=True,blank=True ,choices=nationalityx) 
    dob = models.DateField(max_length=8 , null=True)
    user_type_data=(("freelancer","freelancer"),("client","client"))
    user_type=models.CharField(default="client",choices=user_type_data,max_length=10)
    Profileimg =models.ImageField(default='img/default.jpg',upload_to='profile_pics',blank=True )
    banckacc =models.PositiveBigIntegerField(null=True,blank=True)
    bio =models.TextField(max_length=150,blank=True,null=True,default='')
    followers = models.ManyToManyField("Follow",blank=True,null=True)


def getcurrentusername(instance, filename):
    return "/dir/dir/{0}/{1}".format(instance.user.username, filename)

    
class rateprofile(models.Model):
    user =  models.ForeignKey(CustomUser,related_name='user',on_delete=models.CASCADE )
    rated = models.ForeignKey(CustomUser,related_name='user_rated',on_delete=models.CASCADE )
    rate = models.IntegerField(default=0,blank=True)
    submit = models.BooleanField(default=False)
    def __str__(self) -> str:
        return f"{self.user.username} rate {self.rated.username}"




class freelancer(models.Model):
    person_cats=[
                    ('مصمم ديكور','مصمم ديكور'),('مصمم ديكور تصميم داخلي','مصمم ديكور تصميم داخلي'),('مصمم ديكور تصميم خارجي','مصمم ديكور تصميم خارجي'),
                    ('مصمم جرافيم','مصمم جرافيك'),('UIUX مصمم جرافيك','UIUX مصمم جرافيك'),('مصمم لوجو جرافيك','مصمم لوجو جرافيك'),
                    ('مصمم جرافيك براندينج','مصمم جرافيك براندينج'),('مصمم جرافيك بوستات سوشيال ميديا','مصمم جرافيك بوستات سوشيال ميديا'),('مصمم مواشن جرافيك','مصمم مواشن جرافيك'),
                    ('مصمم موشن جرافيك انيميشن','مصمم موشن جرافيك انيميشن'),('مصمم تايبوجرافي',' مصمم تايبوجرافي')

    
    ]
    
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    objects=models.Manager()
    slug = models.SlugField(blank=True,null=True)
    cat =   models.ManyToManyField('projects.category',default="null",blank=True )
    person_cat =models.CharField( choices=person_cats, max_length=50, blank=True ,null=False )

    def save(self,*args, **kwargs):
        self.slug=slugify(self.user.username)
        super(freelancer,self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username



class client(models.Model):
    user =models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    objects=models.Manager()
    slug = models.SlugField(blank=True,null=True)
    
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.user.username)
        super(client,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.user.username

class Follow(models.Model):
    followed = models.ForeignKey(
        CustomUser,
        related_name='user_followers',
        on_delete=models.CASCADE
    )
    followed_by = models.ForeignKey(
        CustomUser,
        related_name='user_follows',
        on_delete=models.CASCADE
    )


    def __str__(self) -> str:
        return f"{self.followed_by.username} started following {self.followed.username}"



@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type=="freelancer":
            freelancer.objects.create(user=instance,)
        if instance.user_type=="client":
            client.objects.create(user=instance,)

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type=="freelancer":
        instance.freelancer.save()
    if instance.user_type=="client":
        instance.client.save()




class chats(models.Model):
    members = models.ManyToManyField(CustomUser, verbose_name=_("Member"))
 



class Massage(models.Model):
    chat = models.ForeignKey(chats, verbose_name=_("Chat"),on_delete=models.CASCADE ,default=None)
    author = models.ForeignKey(CustomUser, verbose_name=_("User"),on_delete=models.CASCADE ,default=None)
    content = models.TextField(max_length=10000)
    created_on = models.DateTimeField(auto_now_add=True )  
    is_readed = models.BooleanField(_('Readed'), default=False)
    class Meta:
        ordering=['created_on']
 
    def __str__(self):
        return self.content

class contuctus(models.Model):
    user =models.ForeignKey(CustomUser,related_name='needhelp',on_delete=models.CASCADE ,null=True ,blank=True )
    outside_user= models.CharField(max_length=20,null=True ,blank=True)
    email=models.EmailField(null=True ,blank=True)
    title = models.CharField(max_length=20,null=False ,blank=False,default='دعم')
    content = models.TextField()
    
    def __str__(self):
        return self.title

























