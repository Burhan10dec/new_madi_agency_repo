from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('',views.index),
    path('logout',views.logoutuser,name='logout'),
    # path('test',views.AgencyProfileDetailView.test),
    
    # path('test', views.test,name="test"),
    # path('FDWs_profile', views.FDWs_profile),
    # path('myagency', views.myagency),
    path('myagency/<int:pk>', ProfileDetailView.as_view(),name='agency_profile'),
    path('myagency/edit/<int:pk>', ProfileDetailView.as_view()),
    path('myagency/address_edit/<int:pk>',views.update_address,name='address_update'),
    path('myagency/add',views.add_branch,name='add_branch'),
    path('myagency/delete/<int:id>',views.delete_branch,name='delete_branch'),
    # path('myagencyedit', views.myagencyedit),
    path('edit_agency_logo/<int:id>', views.edit_logo,name="edit_agency_logo"),
    path('update_branch/<int:id>', views.update_agency_branch,name="Update_branch"),
    path('edit_office_hours/<int:id>', views.edit_office_hours,name="edit_office_hour"),

    path('media_links', views.edit_media_links,name="media_links"),    
    
# <---------------------------------------------------FDWs urls start------------------------------------------------>
    path('FDWs', views.FDWs,name="fdws"),
    path('FDWs_profile/<int:id>', views.FDWsDetailView,name="fdw_profile"),    
    path('add_FDWs', views.add_FDWs,name="add_FDW"),
    path('edit_image/<int:id>', views.edit_FDW_images,name="edit_FDW_images"),
    path('edit/<int:id>', views.edit_images,name="change"),
    path('add', views.create_FDWs),
    path('edit_FDW/<int:id>', views.edit_FDW,name="edit_FDW"),
    path('edit_FDW/edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete_fdw,name="delete"),
    path('edit_immigration/<int:id>', views.edit_immigration,name="edit_immigration"),
    path('edit_home_country/<int:id>', views.edit_home_country,name="edit_home_country"),
    path('edit_rest_days/<int:id>', views.edit_rest_days,name="edit_rest_days"),
    path('edit_willingness/<int:id>', views.edit_Willingness,name="edit_willingness"),
    path('edit_medical/<int:id>', views.edit_medical,name="edit_medical"),
    path('add/<int:id>', views.add_document,name="add_document"),
    path('edit_fdw_doc/<int:id>', views.edit_document,name="edit_document"),
    path('delete_doc/<int:id>', views.delete_doc,name="delete_doc"),
    # <---------------------------------------------------FDWs urls end------------------------------------------------>

    path('contract', views.contract,name="contracts"),
    # path('users', views.users),
    
    path('add_contract', views.Add_contract),
# <--------------------------------------------------Agents Urls start----------------------------------->
    path('agents', views.view_Agents,name="agents"),
    
    path('Local_Individual',views.add_Agent),
    path('Local_Company',views.add_Agent_Local_Company),    
    path('Overseas_Company',views.add_Agent_Overseas_Company),
    path('Overseas_Individual', views.add_Agent_Overseas_Individual),

    path('edit_individual/<int:id>',views.edit_individual,name='edit_individual_agents'),
    path('save_individual/<int:id>',views.save_individual,name='save_individual_agents'),
    
    path('edit_company/<int:id>',views.edit_company,name='edit_company_agents'),
    path('save_company/<int:id>',views.save_company,name='save_company'),

    path('add_individual', views.create_individual_Agent,name="create_individual_agent"),
    path('add_company', views.create_company_Agent,name="create_company_agent"),

    path('Agent_Details/<int:id>', views.AgentDetailView,name='agent_profile'),    
    path('company_Details/<int:id>', views.CompanyDetailView,name='company_profile'),    
    path('Agent_doc/<int:id>',views.add_agent_document,name="add_agent_document"),
    path('edit_Agent_doc/<int:id>',views.edit_agent_document,name="edit_agent_document"),
    path('delete_agent_doc/<int:id>',views.delete_agent_document,name="delete_agent_doc"),
    
    path('edit_agent_image/<int:id>',views.save_photo,name="save_photo"),    
    path('Edit_Agent_List',views.Edit_Agent_List),

    path('delete_agent/<int:id>',views.delete_agent,name="delete_agent"),
    path('delete_company/<int:id>',views.delete_company,name="delete_company"),
    
# <---------------------------------------------Employer urls start -------------------------------------->
    path('Employers',views.Employers, name="emloyers" ),
    path('add_Employers',views.add_Employers),
    path('Employer_Details',views.Employer_Details),
    path('Edit_Employers',views.Edit_Employers),

# <----------------------------------------------Staff urls start ------------------------------------------>
    path('staff',views.all_staff,name="staffs"),
    path('staff_form',views.add_staff_form,name="add_staff_form"),
    path('add_staff',views.create_staff,name="add_staff"),
    path('edit_staff/<int:id>',views.Edit_staff,name="edit_staff"),
    path('save_staff/<int:id>',views.save_staff,name="save_staff"),
    path('edit_staff_image/<int:id>',views.save_staff_image,name="save_staff_image"),
    path('delete_staff/<int:id>',views.delete_staff,name="delete_staff"),
    path('delete_staff_doc/<int:id>',views.delete_staff_document,name="delete_staff_doc"),

    path('staff_doc/<int:id>',views.add_staff_document,name="add_staff_doc"),
    
    path('staffdetails/<int:id>',views.staffdetails,name="staffdetails"),
    path('Edit_Employers',views.Edit_Employers),
# <----------------------------------------------Staff urls end ------------------------------------------>

# <----------------------------------------------Documents urls start ------------------------------------------>
    path('doc',views.agency_documents,name="doc"),
    path('add_doc',views.add_document_form,name="add_doc"),
    path('delete_agency_doc/<int:id>',views.delete_agency_document,name="delete_agency_doc"),    
    path('agency_doc/<int:id>',views.add_agency_document,name="add_agency_doc"),
    path('edit_agency_doc/<int:id>',views.edit_agency_document,name="edit_agency_document"),
    
# <----------------------------------------------user urls start----------------------------->
    path('Users',views.Users,name="admin-user" ),
    path('user_role', views.user_role,name="user_role"),
    path('admin_add_User',views.add_User,name="add_User"),
    path('edit_User',views.edit_User),

    path('add_user_role',views.user_role,name="user_role"),
    path('User_Management',views.User_Management,name="user_managment"),
]

