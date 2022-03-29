from email import message
from multiprocessing import context
import profile
from pyexpat import model
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from .models import *
from maid_agency.decorators import *
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import ast
# from .form import *

@login_required(login_url="login")
@admin_only
def index(request):
    return render(request,'Dashboard.html',{'user':request.user})


@login_required(login_url="login")
def logoutuser(request):
    logout(request)
    messages.info(request,"Successfully Logout.")
    return redirect('login')

# ------------------ FDWs views start here --------------

@login_required(login_url="login")
@admin_only
def FDWs(request):
    mdws = MDWs.objects.all()
    return render(request,'FDWs/FDWs.html',{'mdws':mdws})


@login_required(login_url="login")
@admin_only
def FDWsDetailView(request,id):
    mdw = MDWs.objects.get(id =id)
    spoken_language_list = ast.literal_eval(mdw.spoken_language)
    
    context = {'data':mdw,'list':spoken_language_list}
    return render(request,'FDWs/FDWs_profile.html',context)


@login_required(login_url="login")
@admin_only
def add_FDWs(request):    
    agents = Agents.objects.filter(agency_username = request.user.profile)
    return render(request,'FDWs/add_FDWs.html',{'agents':agents})


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def create_FDWs(request): 
    fdw_obj = MDWs()
    fdw_obj.maid_name = request.POST.get('maid_name')
    fdw_obj.dob = request.POST.get('dob')
    fdw_obj.country = request.POST.get('nationality')
    fdw_obj.religion = request.POST.get('religion')
    fdw_obj.weight = request.POST.get('weight')
    fdw_obj.martial_status = request.POST.get('marital_status')
    fdw_obj.ref = request.POST.get('ref')
    fdw_obj.maid_type = request.POST.get('type_of_maid')
    fdw_obj.ethic_group = request.POST.get('ethnic_group')
    fdw_obj.education = request.POST.get('education')
    fdw_obj.no_of_children = request.POST.get('no_of_children')
    fdw_obj.no_of_sibling = request.POST.get('no_of_sibling')
    fdw_obj.place_of_birth = request.POST.get('place_of_birth')
    languages = request.POST.getlist('lan[]')
    fdw_obj.spoken_language = str(languages)
    agent_id = request.POST.get('agent_name')  
    fdw_obj.agent_name = Agents.objects.get(id=agent_id)


    # list=[] #myfile is the key of a multi value dictionary, values are the uploaded files
    # for f in request.FILES.getlist('maid_image_1'): #myfile is the name of your html file button
    #     filename = f.name
    #     list.append(filename)

    # fdw_obj.maid_image = request.FILES['maid_image_1'].name
    print(request.FILES.popitem())
    # fdw_obj.save()
    return redirect('fdws')


@login_required(login_url="login")
@admin_only
@require_http_methods(["GET","POST"])
def edit_FDW(request,id):
    obj = MDWs.objects.get(id=id)
    fdw_dob = obj.dob.strftime("%Y-%m-%d")    
    spoken_language_list = ast.literal_eval(obj.spoken_language)
    # print(spoken_language_list)
    agents = Agents.objects.filter(agency_username = request.user.profile)
    return render(request,'FDWs/edit_FDWs.html',{'fdw':obj,'dob':fdw_dob,'agents':agents,'list':spoken_language_list})

@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def edit(request,id): 
    fdw_obj = MDWs.objects.get(id = id)
    fdw_obj.maid_name = request.POST.get('maid_name')
    fdw_obj.dob = request.POST.get('dob')
    fdw_obj.country = request.POST.get('nationality')
    fdw_obj.religion = request.POST.get('religion')
    fdw_obj.weight = request.POST.get('weight')
    fdw_obj.martial_status = request.POST.get('marital_status')
    fdw_obj.ref = request.POST.get('ref')
    fdw_obj.maid_type = request.POST.get('type_of_maid')
    fdw_obj.ethic_group = request.POST.get('ethnic_group')
    fdw_obj.education = request.POST.get('education')
    fdw_obj.no_of_children = request.POST.get('no_of_children')
    fdw_obj.no_of_sibling = request.POST.get('no_of_sibling')
    fdw_obj.place_of_birth = request.POST.get('place_of_birth')    
    languages = request.POST.getlist('lan[]')
    fdw_obj.spoken_language = str(languages)
    agent_id = request.POST.get('agent_name')  
    fdw_obj.agent_name = Agents.objects.get(id=agent_id)
    fdw_obj.save()    
    return redirect('fdws')


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def edit_home_country(request,id):
    fdw = MDWs.objects.get(id=id)
    if Home_country.objects.filter(mdw=fdw).exists():
        hc_obj = Home_country.objects.get(mdw=fdw)
    else:    
        hc_obj = Home_country()
        hc_obj.mdw = fdw
    hc_obj.residential_address = request.POST.get('res_address')
    hc_obj.airport = request.POST.get('airport')
    hc_obj.home_country = request.POST.get('home_country')
    hc_obj.contact_person_name = request.POST.get('contact_person')
    hc_obj.contact_person_no = request.POST.get('contact_person_no')
    hc_obj.contact_person_no_2 = request.POST.get('contact_person_no2')
    hc_obj.email = request.POST.get('email')
    hc_obj.save()
    # messages.success(request, 'home country details has been successfully edited')
    return redirect('fdw_profile',fdw.id)


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def edit_rest_days(request,id):
    # print(request.POST.get('off_day'))    
    fdw = MDWs.objects.get(id=id)
    if Rest_days.objects.filter(mdw=fdw).exists():
        rs_obj = Rest_days.objects.get(mdw=fdw)
    else:    
        rs_obj = Rest_days()
        rs_obj.mdw = fdw
    rs_obj.preferred_no_of_rest_days = request.POST.get('rest_day_no')
    rs_obj.willing_to_work_on_off_days = request.POST.get('off_day')    
    print(request.POST.get('off_day'))
    rs_obj.current_salary = request.POST.get('current_salary')
    rs_obj.expected_salary = request.POST.get('expected_salary')
    rs_obj.remark = request.POST.get('remark')    
    rs_obj.save()
    # messages.success(request, 'home country details has been successfully edited')
    return redirect('fdw_profile',fdw.id)
    # return HttpResponse("Done")



@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def edit_medical(request,id):
    fdw = MDWs.objects.get(id=id)
    if Medical.objects.filter(mdw=fdw).exists():
        md_obj = Medical.objects.get(mdw=fdw)
    else:    
        md_obj = Medical()
        md_obj.mdw = fdw

    md_obj.mental_illness = request.POST.get('mental_illness')
    md_obj.epilepsy = request.POST.get('epilepsy')
    md_obj.asthma = request.POST.get('asthma')
    md_obj.diabetes = request.POST.get('diabetes')
    md_obj.hyper_tension = request.POST.get('hypertension')
    md_obj.tuberculosis = request.POST.get('tuberculosis')
    md_obj.heart_disease = request.POST.get('heart_disease')
    md_obj.maleria = request.POST.get('maleria')
    md_obj.operations = request.POST.get('operations')
    md_obj.allergies = request.POST.get('allergies')
    md_obj.physical_disabilities = request.POST.get('physical_disabilities')
    md_obj.dietary_restrictions = request.POST.get('dietary_res')
    md_obj.others = request.POST.get('others')
    md_obj.save()
    return redirect('fdw_profile',fdw.id)


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def edit_Willingness(request,id):
    fdw = MDWs.objects.get(id=id)
    if Willingness.objects.filter(mdw=fdw).exists():
        wg_obj = Willingness.objects.get(mdw=fdw)
    else:    
        wg_obj = Willingness()
        wg_obj.mdw = fdw
    
    wg_obj.handle_pork = request.POST.get('handle_pork')
    wg_obj.eat_pork = request.POST.get('eat_pork')
    wg_obj.handle_beef = request.POST.get('handle_beef')
    wg_obj.eat_beef = request.POST.get('eat_beef')
    wg_obj.care_pets = request.POST.get('care_pets')
    wg_obj.wash_car = request.POST.get('wash_car')
    wg_obj.gardening_works = request.POST.get('gardening_works')
    wg_obj.save()

    return redirect('fdw_profile',fdw.id)


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def edit_Willingness(request,id):
    fdw = MDWs.objects.get(id=id)
    if Willingness.objects.filter(mdw=fdw).exists():
        wg_obj = Willingness.objects.get(mdw=fdw)
    else:    
        wg_obj = Willingness()
        wg_obj.mdw = fdw


def add_document(requset,id):
    pass


    
@login_required(login_url="login")
@admin_only
def delete_fdw(request,id):
    fdw = MDWs.objects.get(id = id)
    fdw.delete()
    # messages.success(request, 'Maid has been deleted successfully')
    return redirect('fdws')    



# <---------------FDWs views end here--------------------->

# <-----------------Agency views start here---------------> 

@method_decorator(login_required,name='dispatch')
@method_decorator(admin_only,name='dispatch')
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'Agency/My_agency.html'
    context_object_name = 'data'
    pk_url_kwarg = 'pk'       

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)        
        context['branches'] = Branches.objects.all()     
        context['office_hours'] = Office_hours.objects.all()        
        return context
    
    def post(self,request, *args, **kwargs): 
        # user = User.objects.get(id = request.user.id)
        obj =  Profile.objects.get(id = request.user.profile.id)        
        obj.gst_registration = request.POST.get('gst')        
        obj.fiscal_year = request.POST.get('fiscal_year')        
        obj.save()
        return redirect('agency_profile',request.user.profile.id)


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def update_address(request,pk):        
    obj =  Profile.objects.get(id = pk)        
    obj.address = request.POST.get('agency_address')     
    obj.contact_person_name = request.POST.get('agency_contact_person_name')        
    obj.contact_person_number = request.POST.get('agency_mobile')
    # print(request.POST.get('agency_mobile')+''+request.POST.get('agency_address')+' '+request.POST.get('agency_contact_person_name'))
    obj.save()
    return redirect('agency_profile',request.user.profile.id)


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def add_branch(request):          
    agency_obj = Profile.objects.get(agency_username = request.user) 
    print(agency_obj) 
    obj = Branches()  
    obj.agency = agency_obj   
    
    obj.branch_name = request.POST.get('branch_name')
    obj.address = request.POST.get('branch_address')     
    obj.contact_person_name = request.POST.get('contact_person_name')        
    obj.mobile_number1 = request.POST.get('mobile_no1')
    obj.mobile_number2 = request.POST.get('mobile_no2')
    obj.email = request.POST.get('branch_email')
    # print(request.POST.get('agency_mobile')+''+request.POST.get('agency_address')+' '+request.POST.get('agency_contact_person_name'))
    obj.save()
    return redirect('agency_profile',request.user.profile.id)

@login_required(login_url="login")
@admin_only
@require_http_methods(["GET","POST"])
def delete_branch(request,id):          
    branch_obj = Branches.objects.get(id = id)
    branch_obj.delete()
    return redirect('agency_profile',request.user.profile.id)


# <---------------------Agency view end here---------------> 


# <---------------------Agent view end here---------------> 

@login_required(login_url="login")
@admin_only
def view_Agents(request):
    agent = Agents.objects.all()
    # print(type(agent))
    return render(request,'Agents/Agents.html',{'agents':agent})


@method_decorator(login_required,name='dispatch')
@method_decorator(admin_only,name='dispatch')
class AgentDetailView(DetailView):
    model = Agents
    template_name = 'Agents/Agent_Details.html'
    context_object_name = 'agent'
    pk_url_kwarg = 'pk'       

    # def get_context_data(self, **kwargs):
    #     context = super(ProfileDetailView, self).get_context_data(**kwargs)        
    #     context['branches'] = Branches.objects.all()     
    #     context['office_hours'] = Office_hours.objects.all()        
    #     return context
    
    def post(self,request, *args, **kwargs): 
        # user = User.objects.get(id = request.user.id)
        obj =  Profile.objects.get(id = request.user.profile.id)        
        obj.gst_registration = request.POST.get('gst')        
        obj.fiscal_year = request.POST.get('fiscal_year')        
        obj.save()
        return redirect('agency_profile',request.user.profile.id)


def myagencyedit(request):
    return render(request,'Agency/Edit_My_agency.html')

def contract(request):
    return render(request,'Contracts/contracts.html')



def FDWs_profile(request):
    return render(request,'FDWs/FDWs_profile.html')


def user_role(request):
    return render(request,'User/User_role.html')


def Add_contract(request):
    return render(request,'Contracts/Add_contract.html')


# views send by satvik 

def add_Agent(request):
    return render(request,'Agents/add_Agent.html')

def add_Agent_Local_Company(request):
    return render(request,'Agents/add_Agent_Local_Company.html')

# def Agent_Details(request):
#     return render(request,'Agents/Agent_Details.html')

def Agent_Photo(request):
    return render(request,'Agents/Agent_Photo.html')

def add_Agent_Overseas_Company(request):
    return render(request,'Agents/add_Agent_Overseas_Company.html')

def add_Agent_Overseas_Individual(request):
    return render(request,'Agents/add_Agent_Overseas_Individual.html')

def Edit_Agent_List(request):
    return render(request,'Agents/Edit_Agent_List.html')