from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [ 
    path("",views.dashboard,name="dashboard"),
    path("profile_list/",views.profile_list,name="profile_list")
    
]