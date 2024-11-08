from django.urls import path
from . import views

urlpatterns = [
    path("",views.signup,name="signup"),
    path("login/",views.user_login,name="user_login"),
    path("home/",views.home_page,name="home"),
    path("logout/",views.logout_page,name="logout"),
]
