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
    path('myagencyedit', views.myagencyedit),

    path('FDWs', views.FDWs,name="fdws"),
    path('FDWs_profile/<int:id>', views.FDWsDetailView,name="fdw_profile"),    
    path('add_FDWs', views.add_FDWs),
    path('add', views.create_FDWs),
    path('edit_FDW/<int:id>', views.edit_FDW,name="edit_FDW"),
    path('edit_FDW/edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete_fdw,name="delete"),
    path('edit_home_country/<int:id>', views.edit_home_country,name="edit_home_country"),
    path('edit_rest_days/<int:id>', views.edit_rest_days,name="edit_rest_days"),
    path('edit_willingness/<int:id>', views.edit_Willingness,name="edit_willingness"),
    path('edit_medical/<int:id>', views.edit_medical,name="edit_medical"),
    path('add/<int:id>', views.add_document,name="add_document"),
    

    path('contract', views.contract,name="contracts"),
    # path('users', views.users),
    path('user_role', views.user_role,name="user_role"),
    path('add_contract', views.Add_contract),
    path('agents', views.view_Agents,name="agents"),




    path('add_Agent',views.add_Agent),
    path('add_Agent_Local_Company',views.add_Agent_Local_Company),
    
    path('Agent_Details/<int:pk>', AgentDetailView.as_view(),name='agent_profile'),
    # path('Agent_Details',views.Agent_Details),
    path('Agent_Photo',views.Agent_Photo),
    path('add_Agent_Overseas_Company',views.add_Agent_Overseas_Company),
    path('add_Agent_Overseas_Individual', views.add_Agent_Overseas_Individual),
    path('Edit_Agent_List',views.Edit_Agent_List)
]

