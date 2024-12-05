from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path("players/",views.players,name="players"),
    path("players/playerlist/<int:id>",views.playerlist,name="playerlist"),
    path("login/",views.logindata,name="login"),
    path("signup/",views.signup,name="signup"),
    path("userdata/",views.userdata,name="userdata"),
    path("userlogin/",views.userlogin,name="userlogin")
]
