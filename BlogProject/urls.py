"""BlogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
	path("",views.Home,name="home"),
    path("Post/",views.Post,name="Post"),
    path("read/",views.Read,name="read"),
	path("accounts/",include("django.contrib.auth.urls")),
	path("SignUp/",views.SignUp,name="SignUp"),
	path('ChangePassword/',views.User_change_password, name='ChangePassword'),
    # path("SignUpDone/",views.SignUpDone,name="SignUpDone"),
	path('login/',views.dj_login,name="login"), 
	# path('profile/',views.profile_user,name="profile"),
	path("Logout/",views.User_logout, name='Logout'),
     path("update/<int:id>",views.Update,name="update"),
    path("delete/<int:id>",views.Delete,name="delete"),

]
urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
