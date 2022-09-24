from cProfile import label
from dataclasses import fields
from pyexpat import model
from typing_extensions import Self
from django import forms
from .models import CustomUser, Massage, freelancer, rateprofile
from django.utils.translation import ugettext_lazy as _
from django.forms import widgets  
from django.contrib.auth.forms import PasswordChangeForm





class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 


        for fieldname in ['username','first_name','last_name','email','phone_number' ,'nationality','banckacc',]:
            self.fields[fieldname].widget.attrs = {'class': 'form-control'}
            self.fields['bio'].widget.attrs['cols'] = 93
            self.fields['dob'].widget = forms.DateInput(attrs={ 'type': 'date' , 'class': 'form-control'  } )
            self.fields['Profileimg'].widget.attrs = { 'class': 'form-control'  } 
    
    class Meta:
        model = CustomUser
        fields= ['username','first_name','last_name','email','phone_number','dob','bio','nationality','banckacc','Profileimg'] 
        Widgets ={
                        'username' :  forms.TextInput(),
                        'first_name' : forms.TextInput(),
                        'last_name' : forms.TextInput(),
                        'email' :  forms.EmailField(),
                        'phone_number' : forms.IntegerField(),
                        'bio' : forms.TextInput(),
                        }
        labels = {
                        'username' :  _('اسم المستخدم:'),
                        'first_name' :  _('الاسم الاول:'),
                        'last_name' :  _(' اسم العائلة:'),
                        'email' :   _(' البريد الاليكتروني:'),
                        'phone_number' :  _(' :رقم الهاتف:'),
                        'dob' :  _('تاريخ الميلاد:'),
                        'bio' :  _(' نبذه عني:'),
                        'nationality':_(' الجنسية:'),
                        'banckacc':_(' الحساب البنكي:'),
                        'Profileimg':_(''),
                        }  




class FreelancerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
         


        for fieldname in ['person_cat']:
            self.fields[fieldname].widget.attrs = {'class': 'form-control', "cols":95}  
            self.fields['person_cat'].label = 'التصنيف الشخصي:' 
    class Meta:
        model = freelancer
        fields = ['person_cat']
         

class  MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.fields['old_password'].label = 'كلمة المرور الحالية'
        self.fields['new_password1'].label = 'كلمة المرور الجديدة'
        self.fields['new_password2'].label = 'تاكيد كلمة المرور الجديدة '  

        for fieldname in ['old_password','new_password1','new_password2']:
            self.fields[fieldname].widget.attrs = {'class': 'form-control'}   



class massagesform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)     
    
    
        for fieldname in ['content','content']:
            self.fields[fieldname].widget.attrs = {'class': 'form-control', "cols":95}  
            
    class Meta:
        model = Massage
        fields = ['content','content']            

             


class rateprofiles(forms.ModelForm):

            
    class Meta:
        model = rateprofile
        fields = ['user','rated','rate']            
            




