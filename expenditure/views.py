from django.shortcuts import render
from .forms import add_exp,add_adv_form
from .models import advanced
from usersreg.models import member
#Create your views here.


def add_exp_view(request):
    #mem = member.objects.get(user = request.user)
    form = add_exp()
    print(form)
    return render(request,'expenditure/add_exp.html',{'form':form})


#def add_exp_det(request):
#    return render(request,'expenditure/add_exp_det.html')


def generate_exp(request):
    mem = member.objects.get(user = request.user)
    type1 = int(request.POST["type"])
    if type1 == 0:
        mem = member.objects.get(user = request.user)
        adv_obj = advanced(added_by = mem,event_name = request.POST["event_name"], adv_desc = request.POST["adv_desc"],event_date = request.POST["event_date"],amount = request.POST["amount"])
        adv_obj.save()
    if type1 == 1:
        print(request.POST)
        print("expense added")
    return render(request,'expenditure/exp_gen.html',{"type":type1,"member":mem})


def add_adv(request):
    mem = member.objects.get(user = request.user)
    form = add_adv_form()
    print(form)
    return render(request,'expenditure/add_adv.html',{'form':form,"member":mem})


def clear_exp(request):
    mem = member.objects.get(user  = request.user)
    adv_obj = advanced.objects.all()
    print(adv_obj[0].adv_id)
    return render(request,'expenditure/clear_exp.html',{'adv':adv_obj,"member":mem})


def approve_exp(request):
    mem = member.objects.get(user  = request.user)
    return render(request,'expenditure/exp_gen.html',{"member":mem})


def my_exp(request):
    mem = member.objects.get(user  = request.user)
    return render(request,'expenditure/exp_gen.html',{"member":mem})


def view_exp(request):
    mem = member.objects.get(user  = request.user)
    return render(request,'expenditure/exp_gen.html',{"member":mem})