from django.urls import path
from .views import LoginView,LogoutView,UserSignupFormView #,UserUpdateView ,UserDetailView


app_name='users'
urlpatterns = [


    path(route='login/',
         view=LoginView.as_view(),
         name='login'),
    
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/',UserSignupFormView.as_view(),name='signup'),
    # path('update/',UserUpdateView.as_view(),name='update_view_profile'),
    
    # path(
    #     route='<str:username>/',
    #     view=UserDetailView.as_view(),
    #     name='detail'
    # ),
    
]