from django.urls import path
from . import views

urlpatterns = [
    # path('', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('apply_leave/', views.getLeave, name='apply_leave'),
    path('add_leave/', views.addLeave, name='add_leave'),
    path('all_leave/', views.allLeave, name='all_leave'),
    path('new_leave/', views.newLeave, name='new_leave'),
    path('confirm_leave/', views.confirmLeave, name='confirm_leave'),

    path('user_feedback/<int:pd>/', views.userFeedback, name='user_feedback'),

    path('user_profile/', views.userProfile, name='user_profile'),    
    path('all_user/', views.allUser, name='all_user'),
    path('del_user/<int:pd>/', views.delUser, name='del_user'),

   
    path('signup/', views.signUp, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    
]
