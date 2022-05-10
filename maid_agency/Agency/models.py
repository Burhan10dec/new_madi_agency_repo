from email.headerregistry import Address
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class AgencyDetail(models.Model):
    agency = models.OneToOneField(User,on_delete=models.CASCADE)
    agency_name = models.CharField(max_length=50,blank=True)
    license_no = models.CharField(max_length=20)
    uen = models.PositiveIntegerField()
    gst_registration = models.CharField(max_length=20)
    sub_domain_url = models.CharField(max_length=50)
    fiscal_year = models.DateField()
    address = models.CharField(max_length=100,blank=True)
    contact_person_name = models.CharField(max_length=50,blank=True)
    contact_person_number = models.PositiveIntegerField(blank=True,default=12)
    
    # def __str__(self):
    #     return self.agency

# class Branches(models.Model):
#     agency_profile = models.ForeignKey(AgencyProfile)
#     name = models.CharField(max_length=40)
#     telephone = PhoneNumberField(null=False, unique=True)
#     email = models.EmailField(blank=True)
#     house_no = models.CharField(max_length=10)
#     street = models.CharField(max_length=20)
#     city = models.CharField(max_length=20)
#     country = models.CharField(max_length=20)
#     zipcode = models.PositiveIntegerField()


# DAYS_OF_WEEK = (
#     (0, 'Monday'),
#     (1, 'Tuesday'),
#     (2, 'Wednesday'),
#     (3, 'Thursday'),
#     (4, 'Friday'),
#     (5, 'Saturday'),
#     (6, 'Sunday'),
# )

# class office_hours(models.Model):
#     branch = models.ForeignKey(Branches)
#     days = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
#     open_time = models.TimeField()    
#     close_time = models.TimeField()    
#     lunch_start_time = models.TimeField()
#     lunch_end_time = models.TimeField()
    



    

