"""UrBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from BlogApp import views
from django.contrib.auth import views as myauth

urlpatterns = [
    
    path('admin/', admin.site.urls),  
    path('tinymce/', include('tinymce.urls')),
    path('',views.index,name='home'),
    path('category/<str:url>/',views.category,name='category'),
    path('post/<str:url>/',views.post,name='post'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('login/<str:value>/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.Logout_user,name='logout'),
    path('like/',views.like,name='like'),
    path('dislike/',views.dislike,name='dislike'),
    path('passreset/',myauth.PasswordResetView.as_view(template_name='BlogApp/passreset.html',success_url='/passresetdone/'),name='passreset'),
    path('passresetdone/',myauth.PasswordResetDoneView.as_view(template_name='BlogApp/passresetdone.html',),name='passresetdone'),
    path('passwordconfirm/<uidb64>/<token>/',myauth.PasswordResetConfirmView.as_view(template_name='BlogApp/passresetconfirm.html',success_url='/passresetcomplete/'),name='password_reset_confirm'),
    path('passresetcomplete/',myauth.PasswordResetCompleteView.as_view(template_name='BlogApp/passresetcomplete.html'),name='passresetcomplete'),
    path('search/',views.search,name='search'),
    
 


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

