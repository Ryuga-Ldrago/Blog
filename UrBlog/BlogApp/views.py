from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponseRedirect,JsonResponse
from .models import Category,Carosuel,Post,Comment,Like,Dislike
from .forms import Signup,Login,Comment_form
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout
import datetime
from django.views.generic.base import TemplateView
from django.db.models import Q



def search(request):
    
    if request.method == 'POST':
        search_bar=request.POST.get('search')
        # print('search  ==' , search_bar)
        cat=Category.objects.all()
        search_cat_data=Category.objects.filter(Q(title__iexact=search_bar) | Q(title__icontains=search_bar))
        search_post_data=Post.objects.filter(Q(title__iexact=search_bar) | Q(title__icontains=search_bar))
   

        return render(request,'BlogApp/search.html',{'search_cat_data':search_cat_data,'cat':cat,'search_post_data':search_post_data})
    else:
        return redirect(index)

def index(request):
    print('HOme Comes')
    c_data=Carosuel.objects.all()
    cat=Category.objects.all()
    post=Post.objects.all()[:5]
    return render(request,'BlogApp/index.html',{'cat':cat,'c_data':c_data,'posts':post})

def category(request,url):
    cat=Category.objects.all()
    single_cate=Category.objects.get(url=url)
    poster=Post.objects.filter(category=single_cate)
    return render(request,'BlogApp/category.html',{'cat':cat,'single_cate':single_cate,'posts':poster})

def post(request,url):
        if request.method == 'POST':
            fm=Comment_form(request.POST)
            if fm.is_valid():
                msg=fm.cleaned_data['message']
                if request.user.is_authenticated:
                    comm_data=Comment(message=msg,comment_user=request.user,post=Post.objects.get(url=url))
                    comm_data.save()
                    fm=Comment_form()
                else:
                    return redirect(login,value=Post.objects.get(url=url).url)
        else:
            fm=Comment_form()    
        cat=Category.objects.all()
        comment_data=Comment.objects.filter(post=Post.objects.get(url=url))
        post_data=Post.objects.get(url=url)
        c_data=Like.objects.filter(log_post=post_data).count()
        d_c_data=Dislike.objects.filter(log_post_d=post_data).count()

        return render(request,'BlogApp/post.html',{'post_data':post_data,'cat':cat,'comment_data':comment_data,'form':fm,'count_data':c_data,'d_count_data':d_c_data})    

def contact(request):
    cat=Category.objects.all()
    return render(request,'BlogApp/contact.html',{'cat':cat})
def about(request):
    cat=Category.objects.all()
    return render(request,'BlogApp/about.html',{'cat':cat})

def login(request,value=None):
    print('Login Comes')
    cat=Category.objects.all()
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm=Login(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                print('uname',uname)
                print('pname',upass)
                user=authenticate(username=uname,password=upass)
                if user is not None and value == None:  
                    auth_login(request,user)
                    return HttpResponseRedirect('/')
                else: 
                    catch_url=Post.objects.filter(url=value)
                    if catch_url:
                        print(catch_url[0].url)
                        print("filter")
                        auth_login(request,user)
                        return redirect(post,url=catch_url[0].url)
                    else:
                        auth_login(request,user)
                        return HttpResponseRedirect('/')
            else:
                messages.error(request,'Username & Password not Matches. Please, re-enter again')   
                     
        else:
            fm=Login()
        return render(request,'BlogApp/login.html',{'cat':cat,'form':fm,"post_id":id})
    else:
        return HttpResponseRedirect('/')

def Logout_user(request):
    logout(request)
    return redirect(index)

def signup(request):
    cat=Category.objects.all()
    if request.method == 'POST':
      fm=Signup(request.POST)
      if fm.is_valid():
        messages.success(request,'Your account Successfully Created. Now, you go to Login Page')
        fm.save()
        fm=Signup()
        
    else:
        fm=Signup()
    return render(request,'BlogApp/signup.html',{'form':fm,'cat':cat})

def like(request):
    if request.method == 'POST':
        data=request.POST.get('like')
        print("hello")
        print("Like_Post:  =====  ",data)
        p_data=Post.objects.get(url=data)
        if request.user.is_authenticated:
            print("j")
            l_data=Like.objects.filter(log_post=p_data,particular_user=request.user)
            print('l_data ===== @@@@@ ====',l_data.values())
            if l_data:
                l_data[0].delete()
                print("deleted")
                # <!-- Ajax -->
                count_like=str(Like.objects.filter(log_post=p_data).count())
                # return HttpResponse(count_like)
                count_dislike=str(Dislike.objects.filter(log_post_d=p_data).count())
                l_d_dict={'count_like':count_like,'count_dislike':count_dislike}
                return JsonResponse(l_d_dict)
            else:
                like=Like(log_post=p_data,particular_user=request.user,like_btn=True,like_on=datetime.datetime.now())
                d_l_data=Dislike.objects.filter(log_post_d=p_data,particular_user_d=request.user)
                if d_l_data:
                  d_l_data[0].delete()
                like.save()
                print("saved")
                # <!-- Ajax -->
                count_like=str(Like.objects.filter(log_post=p_data).count())
                # return HttpResponse(count_like)
                count_dislike=str(Dislike.objects.filter(log_post_d=p_data).count())
                l_d_dict={'count_like':count_like,'count_dislike':count_dislike}
                return JsonResponse(l_d_dict)     
        else:               
            return redirect(login,value=data)
        return redirect(post,url=data)

def dislike(request):
    if request.method == 'POST':
        data=request.POST.get('dislike')
        print("Like_Post:  =====  ",data)
        p_data=Post.objects.get(url=data)
        # print('POST_DATA === ',p_data)
        if request.user.is_authenticated:
            d_l_data=Dislike.objects.filter(log_post_d=p_data,particular_user_d=request.user)
            print('d_l_data ===== @@@@@ ====',d_l_data.values())
            if d_l_data:
                d_l_data[0].delete()
                print("deleted")
                count_like=str(Like.objects.filter(log_post=p_data).count())
                count_dislike=str(Dislike.objects.filter(log_post_d=p_data).count())
                l_d_dict={'count_like':count_like,'count_dislike':count_dislike}
                return JsonResponse(l_d_dict)
            else:
                
                d_like=Dislike(log_post_d=p_data,particular_user_d=request.user,like_btn_d=True,like_on_d=datetime.datetime.now())
                l_data=Like.objects.filter(log_post=p_data,particular_user=request.user)
                if l_data:
                  l_data[0].delete()
                d_like.save()
                count_dislike=str(Dislike.objects.filter(log_post_d=p_data).count())
                
                count_like=str(Like.objects.filter(log_post=p_data).count())
                l_d_dict={'count_like':count_like,'count_dislike':count_dislike}
                return JsonResponse(l_d_dict)                   
        else:
            return redirect(login,value=data)
        return redirect(post,url=data)



  
