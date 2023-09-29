
from django.urls import path 
from . import views

urlpatterns = [
    path('' ,views.home, name='home'),
    path('profile' ,views.profile, name='profile'),
    path('posts' ,views.Posts, name='posts'),
    path('post/<int:pk>' ,views.Post, name='post'),
    
    # CRUD operations
    path('create' , views.create_post , name='create') ,
    path('edit/<str:pk>' , views.edit_post , name='edit') ,
    path('delete/<str:pk>' , views.delete , name='delete') ,
    path('submit_form/', views.submit_form, name='submit_form'),
    
]
