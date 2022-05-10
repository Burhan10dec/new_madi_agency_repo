from email import message
from multiprocessing import context
import profile
from pyexpat import model
from turtle import title
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
import requests
from .models import *
from maid_agency.decorators import *
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import ast
# from .form import *
from django.core.files.storage import FileSystemStorage
from django.utils.safestring import mark_safe


@login_required(login_url="login")
@admin_only
def index(request):        
    return render(request,'Dashboard.html',{'user':request.user})


@login_required(login_url="login")
def logoutuser(request):
    logout(request)
    messages.info(request,"Successfully Logout.",extra_tags='alert-success')
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
    doc = FDWs_Documents.objects.filter(mdw=mdw)
    context = {'data':mdw,'list':spoken_language_list,'doc':doc}    
    return render(request,'FDWs/FDWs_profile.html',context)


@login_required(login_url="login")
@admin_only
def add_FDWs(request):  
    agents = Agents.objects.filter(agency_username = request.user.profile)
    companies = Agents_company.objects.filter(agency_username = request.user.profile)
    return render(request,'FDWs/add_FDWs.html',{'agents':agents,'companies':companies})    

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
    fdw_obj.height = request.POST.get('height')    
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
    
    if request.POST.get('agent_name'):  
        agent_id = request.POST.get('agent_name')  
        try:
            fdw_obj.agent_name = Agents.objects.get(id=agent_id)
        except:
            pass 
        try:
            fdw_obj.company = Agents_company.objects.get(id=agent_id)
        except:
            pass    
    try:
        fdw_obj.maid_image = request.FILES['maid_image']
    except:
        pass

    try:
        fdw_obj.maid_image_2 = request.FILES['maid_image_2']
    except:
        pass
    
    try:        
        fdw_obj.thumb_image = request.FILES['thumb_image']    
    except:
        return redirect('add_FDW')
    
    fdw_obj.save()
    messages.info(request, mark_safe('FDWs successfully created .'),extra_tags="alert-success")
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
    companies = Agents_company.objects.filter(agency_username = request.user.profile)    
    return render(request,'FDWs/edit_FDWs.html',{'fdw':obj,'dob':fdw_dob,'agents':agents,'companies':companies,'list':spoken_language_list})


@login_required(login_url="login")
@admin_only
def edit_FDW_images(request,id): 
    maid = MDWs.objects.get(id = id)
    return render(request,'FDWs/Edit_FDWs_images.html',{'maid':maid})

@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def edit_images(request,id): 
    fdw_obj = MDWs.objects.get(id=id)    
    try:
        fdw_obj.maid_image = request.FILES['maid_image']
    except:
        pass

    try:
        fdw_obj.maid_image_2 = request.FILES['maid_image_2']
    except:
        pass
    
    try:        
        fdw_obj.thumb_image = request.FILES['thumb_image']    
    except:
        return redirect('edit_FDW_images',id)
    fdw_obj.save()
    messages.info(request, mark_safe('FDWs image successfully updated .'),extra_tags="alert-success")
    return redirect('fdw_profile',id)    


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
    try:
        fdw_obj.agent_name = Agents.objects.get(id=agent_id)
    except:
        pass

    try:
        fdw_obj.company = Agents_company.objects.get(id=agent_id)
    except:
        pass
    
    fdw_obj.save()    
    messages.info(request, mark_safe('FDWs successfully updated .'),extra_tags="alert-success")
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
    messages.info(request, mark_safe('FDWs home country details successfully updated .'),extra_tags="alert-success")    
    return redirect('fdw_profile',fdw.id)


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def edit_immigration(request,id):
    print("in edit")
    mdw_obj = MDWs.objects.get(id = id)
    if Immigration.objects.filter(mdw=mdw_obj).exists():
        obj = Immigration.objects.get(mdw=mdw_obj)
    else:
        obj = Immigration()
    obj.mdw = mdw_obj
    obj.passport_no = request.POST.get('passport_no')
    obj.passport_expiry_date = request.POST.get('pass_exp_date')
    obj.malaysian_id_type = request.POST.get('malaysian_id_type')
    obj.malaysian_id = request.POST.get('malaysian_id')
    obj.imigration_pass_type = request.POST.get('immigration_pass_type')
    obj.svp = request.POST.get('svp')
    obj.work_permit_no = request.POST.get('work_permit_no')
    obj.work_permit_ep_date = request.POST.get('work_permit_ep_date')
    obj.FIN = request.POST.get('fin_no')
    obj.save()
    messages.info(request, mark_safe('FDWs Immigration details successfully updated .'),extra_tags="alert-success")    
    return redirect('fdw_profile',id)


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def edit_rest_days(request,id):    
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
    messages.info(request, mark_safe('FDWs home country details successfully updated .'),extra_tags="alert-success")    
    return redirect('fdw_profile',fdw.id)    


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
    messages.info(request, mark_safe('FDWs medical details successfully updated .'),extra_tags="alert-success")    
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
    messages.info(request, mark_safe('FDWs willingness details successfully updated .'),extra_tags="alert-success")    
    return redirect('fdw_profile',fdw.id)


# @login_required(login_url="login")
# @admin_only
# @require_http_methods(["POST"])
# def edit_Willingness(request,id):
#     fdw = MDWs.objects.get(id=id)
#     if Willingness.objects.filter(mdw=fdw).exists():
#         wg_obj = Willingness.objects.get(mdw=fdw)
#     else:    
#         wg_obj = Willingness()
#         wg_obj.mdw = fdw

@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def add_document(request,id):
    fdw = MDWs.objects.get(id=id)    
    dc_obj = FDWs_Documents()
    if  FDWs_Documents.objects.filter(title = request.POST.get('doc_title')).exists():
        return redirect('fdw_profile',id)
    else:
        dc_obj.mdw = fdw
        dc_obj.title = request.POST.get('doc_title')      
        try:  
            dc_obj.Doc = request.FILES['fdw_document']
        except:
            print("not uploaded")
    
    dc_obj.save()
    messages.info(request, mark_safe('FDWs document successfully added .'),extra_tags="alert-success")    
    return redirect('fdw_profile',fdw.id)


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def edit_document(request,id):
    fdw_doc = FDWs_Documents.objects.get(id=id)    
    fdw_doc.delete()
    new_fdw_doc = FDWs_Documents()
    new_fdw_doc.title = request.POST.get('doc_title')      
    try:  
        new_fdw_doc.Doc = request.FILES['fdw_document']
    except:
        print("not uploaded")
    new_fdw_doc.save()
    messages.info(request, mark_safe('FDWs document details successfully updated .'),extra_tags="alert-success")        
    return redirect('fdw_profile',fdw_doc.mdw.id)


@login_required(login_url="login")
@admin_only
@require_http_methods(["GET","POST"])
def delete_doc(request,id):
    doc = FDWs_Documents.objects.get(id = id)
    doc.delete()
    messages.info(request, mark_safe('FDWs document successfully deleted .'),extra_tags="alert-danger")    
    return redirect('fdw_profile',doc.mdw.id)    


@login_required(login_url="login")
@admin_only
def delete_fdw(request,id):
    fdw = MDWs.objects.get(id = id)
    fdw.delete()
    messages.info(request, mark_safe('FDWs successfully deleted .'),extra_tags="alert-danger")        
    return redirect('fdws')    

# <---------------FDWs views end here---------------------------------------------------->

# <-----------------Agency views start here----------------------------------------------> 

@method_decorator(login_required,name='dispatch')
@method_decorator(admin_only,name='dispatch')
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'Agency/new_My_agency.html'
    context_object_name = 'data'
    pk_url_kwarg = 'pk'       

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)        
        obj =  Profile.objects.get(id = self.kwargs.get('pk'))        
        if Branches.objects.filter(agency = obj).exists():
            context['branches'] = Branches.objects.filter(agency = obj)  
            context['first_branch_name'] = context['branches'][0].branch_name         
        
        if social_media.objects.filter(agency = obj).exists():
            context['links'] = social_media.objects.get(agency = obj)          
        return context
    
    def post(self,request, *args, **kwargs): 
        # user = User.objects.get(id = request.user.id)
        obj =  Profile.objects.get(id = request.user.profile.id)        
        obj.gst_registration = request.POST.get('gst')        
        obj.fiscal_year = request.POST.get('fiscal_year')        
        obj.save()
        messages.info(request, mark_safe('gst registration , fiscal year updated successfully.'),extra_tags="alert-success")
        return redirect('agency_profile',request.user.profile.id)


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def update_address(request,pk):        
    obj =  Profile.objects.get(id = pk)        
    obj.address = request.POST.get('agency_address')     
    obj.contact_person_name = request.POST.get('agency_contact_person_name')        
    obj.contact_person_number = request.POST.get('agency_mobile')    
    obj.save()
    messages.info(request, mark_safe('Address successfully updated.'),extra_tags="alert-success")
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
    messages.info(request, mark_safe('Branch is successfully added.'),extra_tags="alert-success")
    return redirect('agency_profile',request.user.profile.id)

@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def edit_logo(request,id):
    obj = Profile.objects.get(id=id)
    try:
        obj.logo = request.FILES['agency_logo']
        print("dome")
    except:    
        print("not uploaded")
        # return redirect('agent_profile',id)
    obj.save()
    messages.info(request, mark_safe('agency logo successfully changed.'),extra_tags="alert-success")
    return redirect('agency_profile',id)

@login_required(login_url="login")
@admin_only
@require_http_methods(["GET","POST"])
def update_agency_branch(request,id):          
    branch_obj = Branches.objects.get(id = id)        
    branch_obj.agency = Profile.objects.get(agency_username = request.user.id)
    branch_obj.branch_name = request.POST.get('branch_name')
    branch_obj.address = request.POST.get('branch_address')
    branch_obj.contact_person_name = request.POST.get('contact_person_name')
    branch_obj.mobile_number1 = request.POST.get('contact_person_no1')
    branch_obj.mobile_number2 = request.POST.get('contact_person_no2')
    branch_obj.email = request.POST.get('branch_email')
    branch_obj.save()
    messages.info(request, mark_safe('Branch is successfully added.'),extra_tags="alert-success")
    return redirect('agency_profile',request.user.profile.id)


@login_required(login_url="login")
@admin_only
@require_http_methods(["GET","POST"])
def delete_branch(request,id):          
    branch_obj = Branches.objects.get(id = id)
    branch_obj.delete()
    messages.info(request, mark_safe('Branch successfully deleted.'),extra_tags="alert-danger")
    return redirect('agency_profile',request.user.profile.id)

@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def edit_office_hours(request,id):          
    branch_obj = Branches.objects.get(id=id)
    if Office_hours.objects.filter(Branch = branch_obj).exists():
        obj = Office_hours.objects.get(Branch = branch_obj)        
    else:        
        obj = Office_hours()
        obj.Branch = branch_obj

    print(request.POST.get('monday_start'))
    # print(type(datetime.strptime(str(request.POST.get('monday_start')),'%H:%M').time()))
    # obj.monday_start_time = request.POST.get('monday_start')
    if request.POST.get('monday_end'):
        obj.monday_start_time = datetime.strptime(request.POST.get('monday_start'),'%H:%M').time()

    if request.POST.get('monday_end'):
        obj.monday_end_time = datetime.strptime(request.POST.get('monday_end'),'%H:%M').time()
    
    if request.POST.get('tuesday_start'):
        obj.tuesday_start_time = datetime.strptime(request.POST.get('tuesday_start'),'%H:%M').time()

    if request.POST.get('tuesday_end'):
        obj.tuesday_end_time = datetime.strptime(request.POST.get('tuesday_end'),'%H:%M').time()

    if request.POST.get('wednesday_start'):
        obj.wednesday_start_time = datetime.strptime(request.POST.get('wednesday_start'),'%H:%M').time()

    if request.POST.get('wednesday_end'):
        obj.wednesday_end_time = datetime.strptime(request.POST.get('wednesday_end'),'%H:%M').time()

    if request.POST.get('thursday_start'):
        obj.thrusday_start_time = datetime.strptime(request.POST.get('thursday_start'),'%H:%M').time()

    if request.POST.get('thursday_end'):
        obj.thrusday_end_time = datetime.strptime(request.POST.get('thursday_end'),'%H:%M').time()

    if request.POST.get('friday_start'):
        obj.friday_start_time = datetime.strptime(request.POST.get('friday_start'),'%H:%M').time()

    if request.POST.get('friday_end'):
        obj.friday_end_time = datetime.strptime(request.POST.get('friday_end'),'%H:%M').time()

    if request.POST.get('saturday_start'):
        obj.saturday_start_time = datetime.strptime(request.POST.get('saturday_start'),'%H:%M').time()

    if request.POST.get('saturday_end'):
        obj.saturday_end_time = datetime.strptime(request.POST.get('saturday_end'),'%H:%M').time()

    if request.POST.get('sunday_start'):
        obj.sunday_start_time = datetime.strptime(request.POST.get('sunday_start'),'%H:%M').time()

    if request.POST.get('sunday_end'):
        obj.sunday_end_time = datetime.strptime(request.POST.get('sunday_end'),'%H:%M').time()

    if request.POST.get('lunch_start'):
        obj.lunch_start_time = datetime.strptime(request.POST.get('lunch_start'),'%H:%M').time()

    if request.POST.get('lunch_end'):
        obj.lunch_end_time = datetime.strptime(request.POST.get('lunch_end'),'%H:%M').time()
    obj.note = request.POST.get('notes')
    obj.save()
    messages.info(request, mark_safe('office hours successfully edited.'),extra_tags="alert-success")
    return redirect('agency_profile',request.user.profile.id)


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def edit_media_links(request):          
    if social_media.objects.filter(agency = request.user.profile).exists():
        obj = social_media.objects.get(agency = request.user.profile)
    else:
        obj = social_media()
        obj.agency = request.user.profile

    obj.facebook_url = request.POST.get('facebook')
    obj.twiter_url = request.POST.get('twitter')
    obj.instagram_url = request.POST.get('instagram')
    obj.linkedin_url = request.POST.get('linkedin')
    obj.save()
    messages.info(request, mark_safe('social media successfully added.'),extra_tags="alert-success")
    return redirect('agency_profile',request.user.profile.id)

# <--------------------------------------------Agency view end here---------------------------------------> 

# <----------------------------------------Staff views start-------------------------------->
@login_required(login_url="login")
@admin_only
def all_staff(request):
    print(type(request.user.profile))
    # obj = Profile.objects.get(agency_username = request.user)
    staffs = Agency_staff.objects.filter(agency = request.user.profile)
    return render(request,'Staff/stff.html',{'staffs':staffs})    


@login_required(login_url="login")
@admin_only
def add_staff_form(request):    
    branches = Branches.objects.filter(agency = request.user.profile)
    return render(request,'Staff/add_staff.html',{'branches':branches})


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def create_staff(request):    
    obj = Agency_staff()
    obj.agency = request.user.profile    
    obj.staff_name = request.POST.get('staff_name')
    obj.Emp_id = request.POST.get('emp_id')
    try:
        obj.staff_image = request.FILES['staff_image']        
    except:
        messages.info(request, mark_safe('image is not uploaded.'),extra_tags="alert-danger")
        return redirect('staffs')
    obj.Registration = request.POST.get('reg')
    obj.dob = request.POST.get('dob')
    obj.gender = request.POST.get('gender')
    obj.address = request.POST.get('address')
    obj.NRIC = request.POST.get('NRIC')
    obj.citizenship = request.POST.get('citizenship')
    obj.country = request.POST.get('country')
    obj.designation = request.POST.get('designation')
    obj.date_of_joining = request.POST.get('date_of_joining')
    obj.email = request.POST.get('email')
    obj.mobile_no = request.POST.get('mobile_no')    
    obj.branch = request.POST.get('branch')
    obj.save()
    messages.info(request, mark_safe('staff successfully added.'),extra_tags="alert-success")
    return redirect('staffs')


@login_required(login_url="login")
@admin_only
def staffdetails(request,id):
    staff = Agency_staff.objects.get(id = id)
    staff_doc = Staff_Documents.objects.filter(staff = staff)
    return render(request,'Staff/staffdetails.html',{'staff':staff,'staff_docs':staff_doc})


@login_required(login_url="login")
@admin_only
def Edit_staff(request,id):
    staff = Agency_staff.objects.get(id = id)
    dob = staff.dob.strftime("%Y-%m-%d")
    doj = staff.date_of_joining.strftime("%Y-%m-%d")
    branches = Branches.objects.filter(agency = request.user.profile)
    return render(request,'Staff/edit_staff.html',{'staff':staff,'dob':dob,'doj':doj,'branches':branches})


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def save_staff(request,id):    
    obj = Agency_staff.objects.get(id=id)
    obj.agency = request.user.profile    
    obj.staff_name = request.POST.get('staff_name')
    obj.Emp_id = request.POST.get('emp_id')    
    obj.Registration = request.POST.get('reg')
    obj.dob = request.POST.get('dob')
    obj.gender = request.POST.get('gender')
    obj.address = request.POST.get('address')
    obj.NRIC = request.POST.get('NRIC')
    obj.citizenship = request.POST.get('citizenship')
    obj.country = request.POST.get('country')
    obj.designation = request.POST.get('designation')
    obj.date_of_joining = request.POST.get('date_of_joining')
    obj.email = request.POST.get('email')
    obj.mobile_no = request.POST.get('mobile_no')    
    obj.branch = request.POST.get('branch')
    obj.save()
    messages.info(request, mark_safe('staff successfully edited.'),extra_tags="alert-success")
    return redirect('staffs')


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def save_staff_image(request,id):
    obj = Agency_staff.objects.get(id=id)
    try:
        obj.staff_image = request.FILES['staff_image']        
        messages.info(request, mark_safe('Staff image successfully changed.'),extra_tags="alert-success")        
        obj.save()
    except:            
        messages.info(request, mark_safe('Staff image not uploaded.'),extra_tags="alert-danger")        
    return redirect('staffdetails',id)


@login_required
@admin_only
@require_http_methods(["POST"])
def add_staff_document(request,id):
    if  Staff_Documents.objects.filter(title = request.POST.get('doc_title')).exists():
        # agent = Agents.objects.get(id=id)    
        messages.warning(request, mark_safe('Document title already exist'),extra_tags="alert-danger")
        return redirect('staffdetails',id)   
    else:
        doc = Staff_Documents()
        doc.staff = Agency_staff.objects.get(id = id)
        doc.title = request.POST.get('doc_title')
        try:
            doc.doc = request.FILES['staff_doc']
        except:
            print("not uploaded")
    doc.save()
    messages.success(request, mark_safe('<strong>&#128077;</strong> Document has been added successfully'),extra_tags="alert-success")
    return redirect('staffdetails',id)


@login_required(login_url="login")
@admin_only
# @require_http_methods(["Get","POST"])
def delete_staff_document(request,id):
    obj = Staff_Documents.objects.get(id=id)
    obj.delete()
    messages.success(request, mark_safe('<strong>&#128077;</strong> Document has been deleted successfully'),extra_tags="alert-danger")
    return redirect('staffdetails',obj.staff.id)


@login_required(login_url="login")
@admin_only
# @require_http_methods(["Get","POST"])
def delete_staff(request,id):
    obj = Agency_staff.objects.get(id=id)    
    obj.delete()
    messages.info(request, mark_safe('<strong>&#128077;</strong> staff has been deleted successfully'),extra_tags="alert-danger")
    return redirect('staffs')

# <----------------------------------------Staff views end--------------------------------------------------------->

# <-------------------------------------------Agent view start here-----------------------------------------------------> 

@login_required(login_url="login")
@admin_only
def view_Agents(request):
    agent = Agents.objects.all()
    companies = Agents_company.objects.all()
    # print(type(agent))
    return render(request,'Agents/Agents.html',{'agents':agent,'companies':companies})

@login_required(login_url="login")
@admin_only
def AgentDetailView(request,id):
    agent = Agents.objects.get(id =id)    
    maids = MDWs.objects.filter(agent_name = agent)
    if agent.agent_type == 'Local_Individual':
        docs = Agent_Documents.objects.filter(agent = agent)
    context = {'agent':agent,'maids':maids,'docs':docs}    
    return render(request,'Agents/Agent_Details.html',context)


@login_required(login_url="login")
@admin_only
def CompanyDetailView(request,id):
    company = Agents_company.objects.get(id =id)    
    maids = MDWs.objects.filter(company = company)
    # if company.agent_type == 'Local_Company':
    docs = Agent_Documents.objects.filter(company = company)
    context = {'agent':company,'maids':maids,'docs':docs}    
    return render(request,'Agents/Company_details.html',context)


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def create_individual_Agent(request): 
    agent_obj = Agents()
    agent_obj.agency_username = request.user.profile
    agent_obj.agent_name = request.POST.get('agent_name')        
    agent_obj.NRIC = request.POST.get('NRIC')
    agent_obj.agent_registration = request.POST.get('agent_reg')
    agent_obj.country = request.POST.get('country')
    agent_obj.agent_type = request.POST.get('agent_type')
    agent_obj.address = request.POST.get('address')
    agent_obj.contact_person_name = request.POST.get('contact_person_name')
    agent_obj.contact_person_number = request.POST.get('contact_person_no')
    agent_obj.email = request.POST.get('email')
    agent_obj.gender = request.POST.get('gender')
    try:        
        agent_obj.Photo = request.FILES['agent_photo']
    except:
        # return redirect('add_FDW')
        pass
    agent_obj.save()
    return redirect('agents')


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def save_photo(request,id): 
    ag_obj = Agents.objects.get(id=id)
    try:
        ag_obj.Photo = request.FILES['agent_photo']
    except:    
        print("not uploaded")
        # return redirect('agent_profile',id)
    ag_obj.save()
    messages.info(request, mark_safe('Agent Photo successfully changed.'),extra_tags="alert-success")
    return redirect('agent_profile',id)


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def create_company_Agent(request): 
    agent_obj = Agents_company()
    agent_obj.agency_username = request.user.profile
    agent_obj.agent_type = request.POST.get('agent_type')
    agent_obj.company_name = request.POST.get('company_name')
    agent_obj.company_registration = request.POST.get('compnay_ref')
    agent_obj.license = request.POST.get('licence')
    agent_obj.address = request.POST.get('address')
    agent_obj.country = request.POST.get('country')    
    agent_obj.contact_person_name = request.POST.get('contact_person_name')
    agent_obj.contact_person_number = request.POST.get('contact_person_no')
    agent_obj.email = request.POST.get('email')
    agent_obj.website = request.POST.get('website')
    agent_obj.remarks = request.POST.get('remarks')        
    try:        
        agent_obj.logo = request.FILES['logo']
    except:
        print('no photo')                 
    agent_obj.save()
    messages.info(request, mark_safe('Agent successfully added.'),extra_tags="alert-success")
    return redirect('agents')


@login_required
@admin_only
@require_http_methods(["POST"])
def add_agent_document(request,id):
    if  Agent_Documents.objects.filter(title = request.POST.get('doc_title')).exists():
        agent = Agents.objects.get(id=id)    
        messages.warning(request, mark_safe('Document already exist'),extra_tags="alert-warning")
        return redirect('agent_profile',agent.id)   
    else:
        doc = Agent_Documents()
        doc.agent = Agents.objects.get(id = id)
        doc.title = request.POST.get('doc_title')
        try:
            doc.doc = request.FILES['agent_doc']
        except:
            print("not uploaded")
    doc.save()
    messages.success(request, mark_safe('<strong>&#128077;</strong> Document has been added successfully'),extra_tags="alert-success")
    return redirect('agent_profile',id)


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def edit_agent_document(request,id):    
    if  Agent_Documents.objects.filter(title = request.POST.get('doc_title')).exists():
        doc = Agent_Documents.objects.get(id=id)    
        messages.alert(request, mark_safe('Document already exist'))
        return redirect('agent_profile',doc.agent.id)    
    else:
        doc = Agent_Documents.objects.get(id=id)    
        agent = doc.agent        
        doc.delete()
        if agent.agent_type == 'Local - Individual' or agent.agent_type == 'Oversea - Individual':
            new_doc = Agent_Documents()
            new_doc.agent = agent
            new_doc.title = request.POST.get('doc_title')
            try:
                new_doc.doc = request.FILES['agent_doc']
            except:
                print("not uploaded")            
        else:            
            new_doc = Agent_Documents()
            new_doc.company = agent
            new_doc.title = request.POST.get('doc_title')
            try:
                new_doc.doc = request.FILES['agent_doc']
            except:
                print("not uploaded")
            new_doc.save()
    messages.success(request, mark_safe('<strong>&#128077;</strong> Document has been Edited successfully'),extra_tags="alert-success")
    return redirect('agent_profile',agent.id)


@login_required(login_url="login")
@admin_only
# @require_http_methods(["POST"])
def edit_individual(request,id):
    obj = Agents.objects.get(id=id)
    return render(request,'Agents/edit/edit_individual.html',{'obj':obj})


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def save_individual(request,id):
    agent_obj = Agents.objects.get(id=id)
    agent_obj.agency_username = request.user.profile
    agent_obj.agent_name = request.POST.get('agent_name')        
    agent_obj.NRIC = request.POST.get('NRIC')
    agent_obj.agent_registration = request.POST.get('agent_reg')
    agent_obj.country = request.POST.get('country')
    agent_obj.agent_type = 'Local_Individual'
    agent_obj.address = request.POST.get('address')
    agent_obj.contact_person_name = request.POST.get('contact_person_name')
    agent_obj.contact_person_number = request.POST.get('contact_person_no')
    agent_obj.email = request.POST.get('email')
    agent_obj.gender = request.POST.get('gender')    
    
    # try:        
    #     agent_obj.logo = request.FILES['logo']
    # except:
    #     print('no photo')                 
    agent_obj.save()
    messages.warning(request, mark_safe('Agent successfully edited.'),extra_tags="alert-success")
    return redirect('agents')


@login_required(login_url="login")
@admin_only
# @require_http_methods(["POST"])
def edit_company(request,id):    
    obj = Agents_company.objects.get(id=id)
    return render(request,'Agents/edit/edit_company.html',{'obj':obj})


@login_required(login_url="login")
@admin_only
@require_http_methods(["POST"])
def save_company(request,id):
    agent_obj = Agents_company.objects.get(id = id)    
    agent_obj.agency_username = request.user.profile
    # agent_obj.agent_type = obj.agen
    agent_obj.company_name = request.POST.get('company_name')
    agent_obj.company_registration = request.POST.get('compnay_ref')
    agent_obj.license = request.POST.get('licence')
    agent_obj.address = request.POST.get('address')
    agent_obj.country = request.POST.get('country')    
    agent_obj.contact_person_name = request.POST.get('contact_person_name')
    agent_obj.contact_person_number = request.POST.get('contact_person_no')
    agent_obj.email = request.POST.get('email')
    agent_obj.website = request.POST.get('website')
    agent_obj.remarks = request.POST.get('remarks')            
    agent_obj.save()
    messages.warning(request, mark_safe('Agent successfully edited.'),extra_tags="alert-success")
    return redirect('agents')


@login_required(login_url="login")
@admin_only
# @require_http_methods(["Get","POST"])
def delete_agent_document(request,id):
    obj = Agent_Documents.objects.get(id=id)
    obj.delete()
    messages.success(request, mark_safe('<strong>&#128077;</strong> Document has been deleted successfully'),extra_tags="alert-danger")
    return redirect('agents')
    

@login_required(login_url="login")
@admin_only
# @require_http_methods(["Get","POST"])
def delete_agent(request,id):
    obj = Agents.objects.get(id=id)    
    obj.delete()
    messages.success(request, mark_safe('<strong>&#128077;</strong> Agent has been deleted successfully'),extra_tags="alert-danger")
    return redirect('agents')

@login_required(login_url="login")
@admin_only
# @require_http_methods(["Get","POST"])
def delete_company(request,id):
    obj = Agents_company.objects.get(id=id)    
    obj.delete()
    messages.success(request, mark_safe('<strong>&#128077;</strong> Agent has been deleted successfully'),extra_tags="alert-danger")
    return redirect('agents')
        


#-------------- views send by satvik 
@login_required(login_url="login")
@admin_only
def add_Agent(request):
    return render(request,'Agents/local_individual.html')

@login_required(login_url="login")
@admin_only
def add_Agent_Local_Company(request):
    return render(request,'Agents/Local_Company.html')


@login_required(login_url="login")
@admin_only
def add_Agent_Overseas_Company(request):
    return render(request,'Agents/Overseas_Company.html')

@login_required(login_url="login")
@admin_only
def add_Agent_Overseas_Individual(request):
    return render(request,'Agents/Overseas_Individual.html')

@login_required(login_url="login")
@admin_only
def Edit_Agent_List(request):
    return render(request,'Agents/Edit_Agent_List.html')


# <----------------------------------------Agent view End here-----------------------------------------------------> 

def contract(request):
    return render(request,'Contracts/contracts.html')


def Add_contract(request):
    return render(request,'Contracts/Add_contract.html')


# <----------------------------------------Employers views start-------------------------------->
def Employers(request):
    return render(request,'Employers/Employers.html')

def add_Employers(request):
    return render(request,'Employers/add_Employers.html')

def Employer_Details(request):
    return render(request,'Employers/Employer_Details.html')

def Edit_Employers(request):
    return render(request,'Employers/Edit_Employers.html')

# <----------------------------------------Employers views end-------------------------------->



# <----------------------------------------Documents views start-------------------------------->
def agency_documents(request):
    docs = Agency_Documents.objects.filter(agency = request.user.profile)
    return render(request,'Documents/documents.html',{'docs':docs})

def add_document_form(request):
    return render(request,'Documents/adddoc.html')

@login_required
@admin_only
@require_http_methods(["POST"])
def add_agency_document(request,id):
    if  Agency_Documents.objects.filter(title = request.POST.get('doc_title')).exists():
        # agent = Agents.objects.get(id=id)    
        messages.warning(request, mark_safe('Document title already exist'),extra_tags="alert-danger")
        return redirect('doc')   
    else:
        doc = Agency_Documents()
        doc.agency = Profile.objects.get(id = id)
        doc.title = request.POST.get('doc_title')
        try:
            doc.doc = request.FILES['document']
        except:
            print("not uploaded")
    doc.save()
    messages.success(request, mark_safe('<strong>&#128077;</strong> Document has been added successfully'),extra_tags="alert-success")
    return redirect('doc')

@login_required
@admin_only
@require_http_methods(["POST"])
def edit_agency_document(request,id):
    # if  Agency_Documents.objects.filter(title = request.POST.get('doc_title')).exists():    
    #     messages.warning(request, mark_safe('Document title already exist'),extra_tags="alert-danger")
    #     return redirect('doc')   
    # else:
    doc = Agency_Documents.objects.get(id = id)
    # doc.agency = Profile.objects.get(id = id)
    doc.delete()
    doc_new = Agency_Documents()
    doc_new.agency = Profile.objects.get(id = request.user.profile.id) 
    doc_new.title = request.POST.get('doc_title')
    try:
        doc_new.doc = request.FILES['document']
    except:
        print("not uploaded")
    doc_new.save()
    messages.success(request, mark_safe('<strong>&#128077;</strong> Document has been Edited successfully'),extra_tags="alert-success")
    return redirect('doc')



@login_required(login_url="login")
@admin_only
# @require_http_methods(["Get","POST"])
def delete_agency_document(request,id):
    obj = Agency_Documents.objects.get(id=id)
    obj.delete()
    messages.success(request, mark_safe('<strong>&#128077;</strong> Document has been deleted successfully'),extra_tags="alert-danger")
    return redirect('doc')

# <----------------------------------------Documents views End-------------------------------->

# <-----------------user views send by satvik ------------------------------------------->

def Users(request):
    return render(request,'Admin-user/Users.html')

def add_User(request):
    return render(request,"Admin-user/add_User.html")

def edit_User(request):
    return render(request,'Admin-user/edit_User.html')

def user_role(request):
    return render(request,'Admin-user/User_role.html')

def User_Management(request):
    return render(request,'Admin-user/User_Management.html')