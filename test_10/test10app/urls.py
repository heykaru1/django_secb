from django.urls import path
from . import views


urlpatterns = [
    path('',views.index_main),   
    
    path('genders', views.index_gender),
    path('gender/create', views.create_gender),
    path('gender/store', views.store_gender),
    path('gender/show/<int:gender_id>',views.show_gender),
    path('gender/edit/<int:gender_id>',views.edit_gender),
    path('gender/update/<int:gender_id>',views.update_gender),
    path('gender/delete/<int:gender_id>',views.delete_gender),
    path('gender/destroy/<int:gender_id>',views.destroy_gender),
    
    path('users',views.index_user),
    path('user/create',views.create_user),
    path('user/store',views.store_user),
    path('user/show/<int:user_id>',views.show_user),
    path('user/edit/<int:user_id>',views.edit_user),
    path('user/update/<int:user_id>',views.update_user),
    path('user/delete/<int:user_id>',views.delete_user),
    path('user/destroy/<int:user_id>',views.destroy_user),
    
    path('activities',views.index_activities),
    path('activity/create',views.create_activities),
    path('activity/store',views.store_activities),
    path('activity/show/<int:act_id>',views.show_activities),
    path('activity/edit/<int:act_id>',views.edit_activities),
    path('activity/update/<int:act_id>',views.update_activities),
    path('activity/delete/<int:act_id>',views.delete_activities),
    path('activity/destroy/<int:act_id>',views.destroy_activities),
    
    path('incompletes',views.index_incomplete),
    path('incomplete/create',views.create_incomplete),
    path('incomplete/store',views.store_incomplete),
    path('incomplete/show/<int:inc_id>',views.show_incomplete),
    path('incomplete/edit/<int:inc_id>',views.edit_incomplete),
    path('incomplete/update/<int:inc_id>',views.update_incomplete),
    path('incomplete/delete/<int:inc_id>',views.delete_incomplete),
    path('incomplete/destroy/<int:inc_id>',views.destroy_incomplete),
    
    
]