from django.contrib import admin
from django.urls import include, path
from .views import *
from .views import feedback_view, feedback_success_view

urlpatterns = [
    path('',home ,name= 'home'),
    path('blog',blog),
    path('contact',contact,name="contact"),
    path('gallary',gallary),
    path('gallerydetail',gallerydetail),
    path('project',project),
    path('detailproject',detailproject),
    path('privacy',privacy),
    path('termscondition',termscondition),
    path('aboutus',aboutus),
    path('addproject',add_project),
    path('addphotos',add_photos),
    path('allprojects',allproject),
    path('update/<int:id>/', updateproject, name='update'),
    path('delete/<int:id>/', deleteproject, name='delete'),
    path('manageproject',manageproject,name='manageproject'),
    path('messages/', view_messages, name='view_messages'),
    path('register/',registration,name='register'),
    path('login/',login_page,name='login'),
    path('logout/',logout_page,name='logout'),
    path('feedback/', feedback_view, name='feedback'), 
    path('feedback/success/', feedback_success_view, name='feedback_success'),




    
]