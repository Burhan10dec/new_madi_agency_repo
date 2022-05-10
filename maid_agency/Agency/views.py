from email import message
from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from Agency.models import AgencyProfile
from maid_agency.decorators import *
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
@login_required(login_url="login")
@admin_only
def index(request):
    return render(request,'Dashboard.html',{'user':request.user})


@login_required(login_url="login")
def logoutuser(request):
    logout(request)
    messages.info(request,"Successfully Logout.")
    return redirect('login')


# views from frontend project 

def FDWs(request):
    return render(request,'FDWs.html')

# @login_required(login_url="login")
# @admin_only
class AgencyProfileDetailView(DetailView):
    # model = AgencyProfile
    template_name = 'My_agency.html'
    context_object_name = 'data'
    pk_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs): 
        # obj =  AgencyProfile.objects.get(agency = request.user)
        
        # obj.gst_registration = request.POST.get('gst')        
        # obj.fiscal_year = request.POST.get('fiscal_year')
        # obj.save()
        return redirect('agency_profile',request.user.id)

# class AgencyProfileUpdate(UpdateView):
#        model = AgencyProfile
#        fields = ['gst_registration', 'fiscal_year']
#        success_url = reverse_lazy('agency_profile')

def myagencyedit(request):
    return render(request,'Edit_My_agency.html')


def add_FDWs(request):
    return render(request,'add_FDWs.html')

def contract(request):
    return render(request,'contracts.html')

def FDWs_profile(request):
    return render(request,'FDWs_profile.html')


def user_role(request):
    return render(request,'User_role.html')


# def users(request):
#     return render(request,'Users.html')

def Add_contract(request):
    return render(request,'Add_contract.html')