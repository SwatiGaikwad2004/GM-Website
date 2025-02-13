"""
URL configuration for gmwebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from home import views
from home.views import *




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name ='home'),

    path('services/', services, name='services'),
    path('careers/', careers, name='careers'),
    path('about_us/', about_us, name='about_us'),
    path('apply_page/<id>/', apply_page, name='apply_page'),
    path('login_page/', login_page, name='login_page'),
    path('register_page/', register_page, name='register_page'),
    path('logout_page/', logout_page, name='logout_page'),
    path('submit_form/', views.submit_form, name='submit_form'),

    path('culture/', culture, name='culture'),
    path('education/', education, name='education'),
    path('historical_place/', historical_place, name='historical_place'),
    path('facilities/', facilities, name='facilities'),
     

]
