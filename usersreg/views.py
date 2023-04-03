from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import memberCreate
from .models import member
def loginu(request):
    return render(request,'users/login.html')


def logoutu(request):
    logout(request)
    return render(request,'users/logout.html')

def index(request):
    if request.user.is_authenticated:
        mem = member.objects.get(user = request.user)
        return render(request, "users/index.html",{'member':mem})
    else:
        uname = request.POST['loginid']
        passwd = request.POST['passwd']
        user = authenticate(request, username=uname, password=passwd)
        if user is not None:
            login(request,user)
            print('User authentiated')
            mem_con = member.objects.get(user=user)
            return render(request,"users/index.html",{"user":user,"member":mem_con})
        else:
            return render(request, "users/login.html")

def add_mem(request):
    mem = member.objects.get(user = request.user)
    if request.method=='GET':
        form = memberCreate()
        return render(request,'users/add_mem.html',{'form':form,"member":mem})
    if request.method=='POST':
        u_name = request.POST['u_name']
        paswd = request.POST['password']
        email = request.POST['email']
        fname = request.POST['f_name']
        lname = request.POST['l_name']
        type = request.POST['type']
        u = User.objects.create_user(u_name,email,paswd)
        u.first_name = fname
        u.last_name = lname
        u.save()
        mem = member(user=u,type = type)
        mem.save()
        form = memberCreate()
        values=[u_name,paswd,email,fname,lname,type]
        return render(request, 'users/mem_added.html', {'values': values,"member":mem})