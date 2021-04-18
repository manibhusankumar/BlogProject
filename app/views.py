from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import blog
from .forms import blog_form
from django.http import HttpResponse
from . forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login  ,logout,update_session_auth_hash
from django.contrib import messages

# from django.contrib.auth.decorators import login_required

# Create your views here.
def Home(request):
    return render(request,'home.html')
# @login_required(login_url=login)
def dj_login(request):
    if request.method =="POST":
        form =AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname =form.cleaned_data["username"]
            upass =form.cleaned_data["password"]
            user = authenticate(username=uname,password=upass)
            messages.success(request,' successfully Login!!')
            if user is not None:
                login(request,user)
                return redirect('/')
    else:							
        form=AuthenticationForm()
    return render(request,'registration/login.html',{'form':form})			

            
    
# @login_required(login_url=login)
def SignUp(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for'+ user)
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request,"signup.html",{"form":form})


# def SignUpDone(request):
#     return HttpResponse("Acoount Creaeted.!")



# @login_required(login_url=login)
def Post(request):
    if request.method =="POST":
        fm=blog_form(request.POST or None,request.FILES or None)

        if fm.is_valid():
            fm.save()
            return redirect(Read)
    else:
        fm=blog_form()
    return render(request,'post.html',{'form':fm})
    
# @login_required(login_url=login)
def Read(request):
    read=blog.objects.all()
    return render(request,"read.html",{"read":read})


# @login_required(login_url=login)
def Update(request,id):
    upd=blog.objects.get(id=id)
    update=blog_form(request.POST ,request.FILES ,instance=upd)
    if update.is_valid():
        update.save()
        return redirect(Read)
    return render(request,"update.html",{"update":update})   

# @login_required(login_url=login)
def Delete(request,id):
    del_t=blog.objects.get(id=id)    
    del_t.delete()

    return redirect(Read)




# @login_required(login_url=login)
def User_logout(request):
    logout(request)
    messages.success(request,'successfully Logout your account!!')
    return redirect('/')







# def profile_user(request):
    
# 	# if request.user.is_authenticated():
# 	if request.method =='POST':
# 		fm=EditUserProfile(request.POST,instance=request.user)
# 		if fm.is_valid():
# 			fm.save()
# 			messages.success(request,'Your Profile is Updated!!')
# 	else:		
# 		fm = EditUserProfile(instance=request.user)
    
# 	return render(request,'profile.html',{'name':request.user ,'form':fm})


#password change with old passwrod

# @login_required(login_url=login)
def User_change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'congrats your password is change !!')
            return redirect('/')
    else:		
        form = PasswordChangeForm(user=request.user)
    return render(request,'registration/password_change_form.html',{'form':form})


