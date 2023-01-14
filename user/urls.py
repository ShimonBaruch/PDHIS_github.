from user import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register',views.register,name='register'),
    path('logout',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('login',views.login_request,name='login_request'),
]
