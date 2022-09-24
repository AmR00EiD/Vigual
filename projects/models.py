from asyncio.windows_events import NULL
from datetime import datetime
from email.policy import default
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField


class Category(models.Model):
    CATName=models.CharField(max_length=20)
    CATName_arbic=models.CharField(max_length=20,blank=True, null=True)
    slug = models.SlugField(default='all',)
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children' ,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     
   
    def save(self,*args, **kwargs):
        self.slug=slugify(self.CATName)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):                           
        full_path = [self.CATName_arbic]                  
        k = self.parent
        while k is not None:
            full_path.append(k.CATName_arbic)
            k = k.parent
        return ' -> '.join(full_path[::-1])



class projects(models.Model):
    freelancerr =models.ForeignKey('accounts.freelancer', on_delete=models.CASCADE ,null=True,blank=False,related_name="freelancepro")
    Name = models.CharField(max_length=20,null=True)
    Project =models.ImageField(upload_to='media/projects' , default= None)
    other =models.ImageField(upload_to='media/projects' , default= None,blank=True,null=True)
    other2 =models.ImageField(upload_to='media/projects' , default= None,blank=True,null=True)
    other3 =models.ImageField(upload_to='media/projects' , default= None,blank=True,null=True)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE,default= None)
    created_on = models.DateTimeField(auto_now_add=True ,null=True)
    content = models.TextField(blank=True,max_length=1000,)
    rate = models.ValueRange(start=0,end=5,)
    date = models.DateField(max_length=8 , null=True)
    def __str__(self):
        return self.Name









class skills (models.Model):
    Name = models.CharField(max_length=30,unique=True ,primary_key=True)      


    def __str__(self):
            return self.Name




class Post (models.Model):
    author = models.ForeignKey('accounts.client', on_delete= models.CASCADE,)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.content



class Comment (models.Model):
    post = models.ForeignKey(Post,null=True,blank=True,on_delete=models.CASCADE )
    usercomment =models.ForeignKey('accounts.freelancer', on_delete=models.CASCADE ,null=True,blank=False)
    date = models.DateField(max_length=8 , null=True,blank=False)
    cost = models.PositiveIntegerField(null=True,blank=False)
    content = models.TextField(null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)


class orderprocssing (models.Model):
    ordername =models.CharField(max_length=25, null=True,blank=False)
    sender = models.ForeignKey('accounts.freelancer', on_delete=models.CASCADE)
    receiver =models.ForeignKey('accounts.client', on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,)
    created_on = models.DateTimeField(auto_now_add=True)
    deadline =models.DateField(max_length=8 , null=True,blank=False)
    order_cond = models.TextField()
    cost = models.BigIntegerField()
    submit = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    confirm = models.BooleanField(default=False)

    def __str__(self):
        return self.ordername
       





class FinelOrder (models.Model):
    order =models.OneToOneField(orderprocssing, verbose_name=_("orderdetalis"), on_delete=models.CASCADE)
    oredrp =models.FileField(_("order"), upload_to='media/orders', max_length=100)


    def __str__(self):
        return self.order.ordername
       




class Payment(models.Model):
    ord_det =models.ForeignKey(orderprocssing,null=True,on_delete=models.CASCADE )
    card_number = CardNumberField(default=None)
    expire = CardExpiryField(default=None)
    security_code = SecurityCodeField(default=None)
    
                