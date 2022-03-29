from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
from .views import AgencyProfileDetailView
urlpatterns = [
    path('',views.index),
    path('logout',views.logoutuser),

    # path('test',views.AgencyProfileDetailView.test),


    path('FDWs', views.FDWs,name="fdws"),
    path('add_FDWs', views.add_FDWs),
    path('FDWs_profile', views.FDWs_profile),
    # path('myagency', views.myagency),
    path('myagency/<int:pk>', AgencyProfileDetailView.as_view(),name='agency_profile'),
    path('myagency/edit', AgencyProfileDetailView.as_view()),
    path('myagencyedit', views.myagencyedit),
    path('contract', views.contract,name="contracts"),
    # path('users', views.users),
    path('user_role', views.user_role,name="user_role"),
    path('add_contract', views.Add_contract),
]

