from dataclasses import field, fields
from pyexpat import model
from typing_extensions import Self
from urllib import request
from django import forms

from accounts.models import CustomUser, freelancer
from .models import *
from django.utils.translation import ugettext_lazy as _


class ProjectsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 

        self.fields['date'].widget = forms.DateInput(attrs={ 'type': 'date' , 'class': 'form-control form-control-lg'  } )
        self.fields['Project'].widget.attrs = { 'class': 'form-control'  } 
        self.fields['other'].widget.attrs = { 'class': 'form-control'  } 
        self.fields['other2'].widget.attrs = { 'class': 'form-control'  } 
        self.fields['other3'].widget.attrs = { 'class': 'form-control'  } 
        for fieldname in ['Name','cat','content']:
            self.fields[fieldname].widget.attrs = {'class': 'form-control'}
    
    class Meta:
        model = projects
        fields =[
            'Name',
            'Project',
            'cat',
            'content',
            'other',
            'other2',
            'other3',
            'date'
        ]
  
        Widgets ={
             'Name' :  forms.TextInput(attrs={'class': 'form-control'}),
             'Project' : forms.FileInput(attrs={'class':'form-control'}),
             'cat' : forms.Select(attrs={'class':'form-control'}),}
        labels = {
            'Name': _('اسم المشروع'), 
            'Project': _(' المشروع'),
            'cat': _('التصنيف'), 
            'content': _('وصف المشروع'), 
            'other': _(' المشروع'),
            'other2': _('المشروع'), 
            'other3': _('المشروع'),
            
            
            
            }  


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): 
            super(PostForm, self).__init__(*args, **kwargs)
            self.fields['content'].widget.attrs['cols'] = 127  
    
    
    class  Meta:
        model = Post
        fields = [
            'content' ]



class finalorders(forms.ModelForm):
    def __init__(self,*args,user,pay,done,pk, **kwargs):
        super(finalorders, self).__init__(*args, **kwargs) 
        
        self.fields['order'].queryset  = orderprocssing.objects.filter(sender__user=user,paid=pay,submit=done,id=pk)
        
        for fieldname in ['order','oredrp' ]:
            self.fields[fieldname].widget.attrs = {'class': 'form-control '}

    
    class  Meta:
        model = FinelOrder 
        fields = ['order' ,'oredrp',]
        Widgets ={
             'order' :  forms.Select(),
             'oredrp' : forms.FileInput(),}                       




class commentsform(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(commentsform, self).__init__(*args, **kwargs) 
        self.fields['cost'].widget.attrs = {'class': 'form-control form-control-lg ',}
        self.fields['date'].widget = forms.DateInput(attrs={ 'type': 'date' , 'class': 'form-control form-control-lg'  } )
        self.fields['content'].widget.attrs['cols'] = 120  
    class  Meta:
        model = Comment 
        fields = ['date','cost','content']

class orderprocssingform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 


        for fieldname in ['ordername','category','order_cond','cost','receiver']:
            self.fields[fieldname].widget.attrs = {'class': 'form-control'}  
            self.fields['deadline'].widget = forms.DateInput(attrs={ 'type': 'date' , 'class': 'form-control'  } ) 
    
    
    
    
    
    class Meta:
        model =orderprocssing
        fields = ['ordername','category','deadline','order_cond','cost','receiver']



   





