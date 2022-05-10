from datetime import datetime
from distutils.command.upload import upload
import email
from email.headerregistry import Address
from email.policy import default
from fileinput import filename
from pyexpat import model
from secrets import choice
from xml.dom.minidom import Document
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from phonenumber_field.modelfields import PhoneNumberField
import os
from uuid import uuid4

# Create your models here.
#<----------------------------------------Agency models start ---------------------------->
def Agency_images_path_and_rename(instance, filename):
    upload_to = 'Agency/images/'
    ext = filename.split('.')[-1]    
    filename = '{}.{}'.format(uuid4().hex, ext)    
    return os.path.join(upload_to, filename)


class Profile(models.Model):
    agency_username = models.OneToOneField(User,on_delete=models.CASCADE)
    agency_name = models.CharField(max_length=50,blank=True)
    license_no = models.CharField(max_length=20)
    uen = models.PositiveIntegerField()
    gst_registration = models.CharField(max_length=20)
    sub_domain_url = models.CharField(max_length=50)
    fiscal_year = models.DateField()
    address = models.CharField(max_length=100,blank=True)
    contact_person_name = models.CharField(max_length=50,blank=True)
    contact_person_number = PhoneNumberField(blank=True,default=12)
    logo = models.ImageField(upload_to=Agency_images_path_and_rename,null=True,blank=True,default='Agency/images/blank_logo.png')
    website = models.CharField(max_length=50,null=True,blank=True,default="www.xyz.com")

    def __str__(self):
        return self.agency_name


class Branches(models.Model):
    agency = models.ForeignKey(Profile,on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    contact_person_name = models.CharField(max_length=50,blank=True)
    mobile_number1 = models.PositiveIntegerField(blank=True,null=True,default=00)
    mobile_number2 = models.PositiveIntegerField(blank=True,null=True,default=00)
    email = models.EmailField(blank=True,null=True)


    def __str__(self):
        return self.branch_name


class Office_hours(models.Model):
    Branch = models.OneToOneField(Branches,on_delete=models.CASCADE)
    monday_start_time = models.TimeField(max_length=20,blank=True,null=True)
    monday_end_time = models.TimeField(blank=True,null=True)
    tuesday_start_time = models.TimeField(blank=True,null=True)
    tuesday_end_time = models.TimeField(blank=True,null=True)
    wednesday_start_time = models.TimeField(blank=True,null=True)
    wednesday_end_time = models.TimeField(blank=True,null=True)
    thrusday_start_time = models.TimeField(blank=True,null=True)
    thrusday_end_time = models.TimeField(blank=True,null=True)
    friday_start_time = models.TimeField(blank=True,null=True)
    friday_end_time = models.TimeField(blank=True,null=True)
    saturday_start_time = models.TimeField(blank=True,null=True)
    saturday_end_time = models.TimeField(blank=True,null=True)
    sunday_start_time = models.TimeField(blank=True,null=True)
    sunday_end_time = models.TimeField(blank=True,null=True)
    lunch_start_time = models.TimeField(blank=True,null=True)
    lunch_end_time = models.TimeField(blank=True,null=True)
    note = models.CharField(max_length=100,blank=True)
    
    def __str__(self):
        return self.Branch 

class social_media(models.Model):
    agency = models.OneToOneField(Profile,on_delete=models.CASCADE)
    facebook_url = models.URLField(max_length=500,null=True,blank=True)
    instagram_url = models.URLField(max_length=500,null=True,blank=True)
    linkedin_url = models.URLField(max_length=500,null=True,blank=True)
    twiter_url = models.URLField(max_length=500,null=True,blank=True)
    
#<----------------------------------------Agency models End ---------------------------->

#<----------------------------------------Staff models start ---------------------------->
def Staff_images_path_and_rename(instance, filename):
    upload_to = 'Staff/images/'
    ext = filename.split('.')[-1]    
    filename = '{}.{}'.format(uuid4().hex, ext)    
    return os.path.join(upload_to, filename)

class Agency_staff(models.Model):
    agency = models.ForeignKey(Profile,on_delete=models.CASCADE)
    staff_name = models.CharField(max_length=50,blank=True,null=True)
    Emp_id = models.CharField(max_length=50,blank=True,null=True)
    staff_image = models.ImageField(upload_to=Staff_images_path_and_rename,null=True,blank=True)
    Registration = models.CharField(max_length=50,blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    gender_choice = (
        ('Male','Male'),
        ('Female','Female'),
    )    
    gender = models.CharField(max_length=6,choices=gender_choice,null=True,blank=True)
    NRIC = models.CharField(max_length=20,blank=True,null=True)
    citizenship = models.CharField(max_length=50,blank=True,null=True)
    country = models.CharField(max_length=20,blank=True,null=True)
    designation = models.CharField(max_length=20,blank=True,null=True)
    date_of_joining = models.DateField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    mobile_no = models.PositiveIntegerField(blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    branch = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.staff_name
    

def Staff_document_path_and_rename(instance, filename):
    upload_to = 'Staff/documents/'
    ext = filename.split('.')[-1]    
    filename = '{}.{}'.format(uuid4().hex, ext)    
    return os.path.join(upload_to, filename)

class Staff_Documents(models.Model):
    staff = models.ForeignKey(Agency_staff,on_delete=models.CASCADE,blank=True,null=True)    
    title = models.CharField(max_length=50,blank=True,null=True)    
    doc = models.FileField(upload_to=Staff_document_path_and_rename,blank=True,null=True)   

    def __str__(self):
        return self.title

#<----------------------------------------Staff models end ---------------------------->

#<----------------------------------------Agents models start ---------------------------->
def Agents_images_path_and_rename(instance, filename):
    upload_to = 'Agents/images/'
    ext = filename.split('.')[-1]    
    filename = '{}.{}'.format(uuid4().hex, ext)    
    return os.path.join(upload_to, filename)

class Agents(models.Model):
    agency_username = models.ForeignKey(Profile,on_delete=models.CASCADE)
    agent_name = models.CharField(max_length=50,blank=True)
    Photo = models.ImageField(upload_to=Agents_images_path_and_rename,null=True,blank=True)
    agent_type = models.CharField(max_length=50,blank=True,null=True)
    gender_choice = (
        ('Male','Male'),
        ('Female','Female'),
    )
    gender = models.CharField(max_length=6,choices=gender_choice,null=True,blank=True,default='Female')    
    NRIC = models.CharField(max_length=20,blank=True)
    agent_registration = models.CharField(max_length=50,blank=True,null=True)
    country = models.CharField(max_length=20,blank=True,null=True)
    agent_type = models.CharField(max_length=20,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    contact_person_name = models.CharField(max_length=50,blank=True,null=True)
    contact_person_number = models.PositiveIntegerField(blank=True,null=True,default=0)
    email = models.EmailField(blank=True,null=True)
    
    def __str__(self):
        return self.agent_name


class Agents_company(models.Model):
    agency_username = models.ForeignKey(Profile,on_delete=models.CASCADE)
    agent_type = models.CharField(max_length=50,blank=True,null=True)
    company_name = models.CharField(max_length=50,blank=True)
    company_registration = models.CharField(max_length=50,blank=True,null=True)
    license = models.CharField(max_length=50,blank=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    country = models.CharField(max_length=20,blank=True,null=True)
    logo = models.ImageField(upload_to=Agents_images_path_and_rename,null=True,blank=True)    
    contact_person_name = models.CharField(max_length=50,blank=True,null=True)
    contact_person_number = models.PositiveIntegerField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    website = models.CharField(max_length=50,blank=True,null=True)
    remarks = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.company_name


class contact_list(models.Model):
    company = models.ForeignKey(Agents_company,on_delete=models.CASCADE)
    salutation_choice = (
        ('Mr','Mr'),
        ('Mrs','Mrs'),
        ('Ms','Ms'),
        ('Mdm','Mdm'),
        ('Dr','Dr'),
    )
    salutation = models.CharField(choices=salutation_choice,blank=True,null=True,max_length=4)
    name = models.CharField(max_length=50,blank=True,null=True)
    designation = models.CharField(max_length=50,blank=True,null=True)
    work_phone = models.PositiveIntegerField(blank=True,null=True)
    mobile_no = models.PositiveIntegerField(blank=True,null=True)    
    Email = models.EmailField(blank=True,null=True)
    primary = models.BooleanField(blank=True,null=True)

    def __str__(self):
        return self.company

def Agent_document_path_and_rename(instance, filename):
    upload_to = 'Agents/documents/'
    ext = filename.split('.')[-1]    
    filename = '{}.{}'.format(uuid4().hex, ext)    
    return os.path.join(upload_to, filename)

class Agent_Documents(models.Model):
    agent = models.ForeignKey(Agents,on_delete=models.CASCADE,blank=True,null=True)
    company = models.ForeignKey(Agents_company,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=50,blank=True,null=True)    
    doc = models.FileField(upload_to=Agent_document_path_and_rename,blank=True,null=True)   

    def __str__(self):
        return self.title


#<----------------------------------------Agents models End ---------------------------->

#<----------------------------------------MDWs models start ---------------------------->

def MDWs_images_path_and_rename(instance, filename):
    upload_to = 'MDWs/images/'
    ext = filename.split('.')[-1]    
    filename = '{}.{}'.format(uuid4().hex, ext)    
    return os.path.join(upload_to, filename)

class MDWs(models.Model):
    agent_name = models.ForeignKey(Agents,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(Agents_company,on_delete=models.CASCADE,blank=True,null=True)
    maid_name = models.CharField(max_length=50,blank=True)
    maid_image = models.ImageField(upload_to=MDWs_images_path_and_rename,null=True,blank=True)
    maid_image_2 = models.ImageField(upload_to=MDWs_images_path_and_rename,null=True,blank=True)
    thumb_image = models.ImageField(upload_to=MDWs_images_path_and_rename,null=True,blank=True)
    
    dob = models.DateField()
    ref = models.CharField(max_length=50)
    maid_type = models.CharField(max_length=20)
    ethic_group = models.CharField(max_length=20,blank=True,null=True)
    country = models.CharField(max_length=50)
    religion = models.CharField(max_length=50,null=True)
    height = models.PositiveBigIntegerField(blank=True,null=True)
    weight = models.PositiveBigIntegerField(blank=True,null=True)
    education = models.CharField(max_length=100)
    no_of_sibling = models.PositiveBigIntegerField(blank=True,null=True)
    no_of_children = models.PositiveBigIntegerField(blank=True,null=True)
    martial_status = models.CharField(max_length=50,blank=True,null=True)
    ages_of_children = models.CharField(max_length=100,blank=True,null=True)
    place_of_birth = models.CharField(max_length=50,blank=True,null=True)    
    spoken_language = models.CharField(max_length=500,blank=True,null=True)
           
    def __str__(self):
        return self.maid_name


class Immigration(models.Model):
    mdw = models.OneToOneField(MDWs,on_delete=models.CASCADE)
    passport_no = models.CharField(max_length=50)
    passport_expiry_date = models.DateField()    
    malaysian_id_type = models.CharField(max_length=50,blank=True,null=True)
    malaysian_id = models.CharField(max_length=50,blank=True,null=True)
    imigration_pass_type  = models.CharField(max_length=50,blank=True,null=True)
    svp = models.DateField(blank=True,null=True)
    work_permit_no = models.CharField(max_length=50,blank=True,null=True)
    work_permit_ep_date = models.DateField()
    FIN = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.mdw


class Home_country(models.Model):
    mdw = models.OneToOneField(MDWs,on_delete=models.CASCADE)
    residential_address = models.CharField(max_length=50,blank=True,null=True)
    airport = models.CharField(max_length=50,blank=True,null=True)        
    home_country = models.CharField(max_length=50,blank=True,null=True)        
    contact_person_name = models.CharField(max_length=50,blank=True,null=True)       
    contact_person_no = models.PositiveIntegerField(blank=True,null=True)       
    contact_person_no_2 = models.PositiveIntegerField(blank=True,null=True)       
    email = models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.mdw


class Medical(models.Model):
    mdw = models.OneToOneField(MDWs,on_delete=models.CASCADE)
    mental_illness = models.BooleanField(blank=True,null=True)    
    epilepsy = models.BooleanField(blank=True,null=True)   
    asthma = models.BooleanField(blank=True,null=True)   
    diabetes = models.BooleanField(blank=True,null=True)   
    hyper_tension = models.BooleanField(blank=True,null=True)   
    tuberculosis = models.BooleanField(blank=True,null=True)    
    heart_disease = models.BooleanField(blank=True,null=True)    
    maleria = models.BooleanField(blank=True,null=True)    
    operations = models.BooleanField(blank=True,null=True)    
    allergies = models.CharField(max_length=100,blank=True,null=True)    
    physical_disabilities = models.CharField(max_length=100,blank=True,null=True)    
    dietary_restrictions = models.CharField(max_length=100,blank=True,null=True)        
    others = models.CharField(max_length=100,blank=True,null=True)    

    def __str__(self): 
        return self.mdw

class Rest_days(models.Model):
    mdw = models.OneToOneField(MDWs,on_delete=models.CASCADE)
    preferred_no_of_rest_days = models.PositiveIntegerField()        
    willing_to_work_on_off_days = models.BooleanField(blank=True,null=True)
    current_salary = models.CharField(max_length=10,blank=True,null=True)
    expected_salary = models.CharField(max_length=10,blank=True,null=True)
    remark = models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return self.mdw


class Willingness(models.Model):
    mdw = models.OneToOneField(MDWs,on_delete=models.CASCADE)
    handle_pork = models.BooleanField(blank=True,null=True)    
    eat_pork = models.BooleanField(blank=True,null=True)   
    handle_beef = models.BooleanField(blank=True,null=True)   
    eat_beef = models.BooleanField(blank=True,null=True)   
    care_pets = models.BooleanField(blank=True,null=True)   
    wash_car = models.BooleanField(blank=True,null=True)    
    gardening_works = models.BooleanField(blank=True,null=True)        

    def __str__(self):
        return self.mdw


def MDWs_document_path_and_rename(instance, filename):
    upload_to = 'MDWs/document/'
    ext = filename.split('.')[-1]    
    filename = '{}.{}'.format(uuid4().hex, ext)    
    return os.path.join(upload_to, filename)

class FDWs_Documents(models.Model):
    mdw = models.ForeignKey(MDWs,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True,null=True)    
    Doc = models.FileField(upload_to=MDWs_document_path_and_rename,blank=True,null=True)   

    def __str__(self):
        return self.title

#<----------------------------------------MDWs models end ---------------------------->
#<----------------------------------------Agency_documents models start ---------------------------->

def Agency_document_path_and_rename(instance, filename):
    upload_to = 'Documents'
    ext = filename.split('.')[-1]    
    filename = '{}.{}'.format(uuid4().hex, ext)    
    return os.path.join(upload_to, filename)

class Agency_Documents(models.Model):
    agency = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)    
    title = models.CharField(max_length=50,blank=True,null=True)    
    doc = models.FileField(upload_to=Agency_document_path_and_rename,blank=True,null=True)   

    def __str__(self):
        return self.title