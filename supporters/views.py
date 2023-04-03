from django.shortcuts import render
from .models import supporter
from donation.models import verified_donation
import django.db.utils
from . import forms
from django.http import HttpResponse,FileResponse
from openpyexcel import load_workbook,Workbook
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from usersreg.models import member
# Create your views here.

@login_required
def add_supp(request):
    mem = member.objects.get(user = request.user)
    if request.method == 'POST':
        form = forms.AddSupp(request.POST)
        if form.is_valid():
            form.clean()
            new_supp = form.save(commit = False)
            new_supp.dob = request.POST['dob']
            new_supp.save()
            form = forms.AddSupp()
            return render(request, 'supp/add_supp.html', {'form': form,'messages':'Member Saved Successfully',"member":mem})
        else: 
            return render(request, 'supp/add_supp.html', {'form': form,'messages':'Oops there seems to be some problem wit the data you eltered!!!',"member":mem})
    else:
        form = forms.AddSupp()
        return render(request, 'supp/add_supp.html', {'form':form,'messages':'0',"member":mem})


@login_required
def edit_supp(request):
    mem = member.objects.get(user = request.user)
    if request.method == 'GET':
        supp = supporter.objects.all()
        context={
            'supp':supp,
            'view':'edit',
            'member':mem
        }
        return render(request,'supp/edit_spp.html',context)
    if request.method == "POST":
        value = request.POST['supp_name']
        print(value)
        value = value.split(',')
        ph = value[1]
        na = value[0]
        obj = supporter.objects.get(name=na, phone_no=ph)
        form = forms.AddSupp()
        form.fields['name'].label = 'Name:'+str(obj.name)
        form.fields['age'].label = 'Age:'+str(obj.age)
        form.fields['gender'].label = 'Gender:'+str(obj.gender)
        form.fields['phone_no'].label =  'Phone No:'+str(obj.phone_no)
        form.fields['phone_no'].required = False
        form.fields['alt_phone_no'].label =  'Alternate Phone No:'+str(obj.alt_phone_no)
        form.fields['email_id'].label =   'Email:'+str(obj.email_id)
        form.fields['city'].label =   'City:'+str(obj.city)
        form.fields['Reference'].label =  'Reference:'+str(obj.Reference)
        form.fields['pan_card'].label =   'Pan Card:'+str(obj.pan_card)
        form.fields['address_a'].label =   'Address:'+str(obj.address_a)
        form.fields['is_constant'].label =   'Constant:'+str(obj.is_constant)
        form.fields['amount'].label =   'Amount:'+str(obj.amount)
        form.fields['is_sponsor'].label =   'Child Sponsor:'+str(obj.is_sponsor)
        form.fields['sponsee'].label =  'Child:'+str(obj.sponsee)
        form.fields['is_one_time'].label =  'One Time:'+str(obj.is_one_time)
        form.fields['resources'].label =  'Resources:'+str(obj.resources)
        form.fields['is_si'].label =   'SI:'+str(obj.is_si)
        form.fields['si_date'].label =  'SI Date:'+str(obj.si_date)
        form.fields['profession'].label = 'Profession:'+str(obj.profession)
        return render(request, 'supp/edit_supp_form.html', {'form':form,'messages':'0','member': mem,"obj":obj})


@login_required
def supp_edited(request):
    mem = member.objects.get(user = request.user)
    if request.method == 'POST':
        print(request.POST)
        form = forms.AddSupp(request.POST)
        keys = form.changed_data
        mem_id = request.POST["pk"]
        obj = supporter.objects.get(pk=mem_id)
        if 'name' in keys:
            obj.name = request.POST['name']
        if 'age' in keys:
            obj.age = request.POST['age']
        if 'gender' in keys:
            obj.gender = request.POST['gender']
        if 'phone_no' in keys:
            obj.phone_no = request.POST['phone_no']
        if 'alt_phone_no' in keys:
            obj.alt_phone_no = request.POST['alt_phone_no']
        if 'email_id' in keys:
            obj.email_id = request.POST['email_id']
        if 'city' in keys:
            obj.city = request.POST['city']
        if 'Reference' in keys:
            obj.Reference = request.POST['Reference']
        if 'pan_card' in keys:
            obj.pan_card = request.POST['pan_card']
        if 'address_a' in keys:
            obj.address_a = request.POST['address_a']
        if 'is_constant' in keys:
            if request.POST['is_constant'] == "on":
                obj.is_constant = not(obj.is_constant)
                if obj.is_constant == False:
                    obj.amouunt = 0
                else:
                    try:
                        obj.amount = request.POST['amount']
                    except:
                        pass
        if 'is_sponsor' in keys:
            if request.POST['is_sponsor'] == "on":
                obj.is_sponsor = not(obj.is_sponsor)
                if obj.is_sponsor == False:
                    obj.sponsee = ""
                else:
                    try:
                        obj.sponsee = request.POST['sponsee']
                    except:
                        pass
        if 'is_one_time' in keys:
            if request.POST['is_one_time'] == "on":
                obj.is_one_time = not(obj.is_one_time)
        if 'resources' in keys:
            if request.POST['resources'] == "on":
                obj.resources = not(obj.resources)
        if 'is_si' in keys:
            if request.POST['is_si']=="on":
                obj.is_si = not(obj.is_si)
                if obj.is_si == False:
                    obj.si_date = 0
                else:
                    try:
                        obj.si_date = request.POST['si_date']
                        obj.is_constant = True
                        obj.amount = request.POST["amount"]
                    except:
                        pass
        if 'dob' in keys:
            obj.dob = request.POST['dob']
        if 'profession' in keys:
            obj.profession = request.POST['profession']
        obj.save()
        return render(request,'supp/supp_edited.html',{"member":mem})


@login_required
def del_supp(request):
    mem = member.objects.get(user = request.user)
    if request.method == 'GET':
        supp = supporter.objects.all()
        context = {
            'supp': supp,
            'view':'delete',
            "member":mem
        }
        return render(request, 'supp/edit_spp.html', context)
    if request.method == 'POST':
        value = request.POST['supp_name']
        print(value)
        value = value.split(',')
        ph = value[1]
        print(ph)
        na = value[0]
        print(value, ph, na)
        obj = supporter.objects.get(name=na, phone_no=ph)
        context = {
            'supp':obj,
            'view':'delete',
            "member":mem
        }
    return render(request,'supp/detail.html',context)


@login_required
def delete(request):
    mem = member.objects.get(user = request.user)
    ph = (request.POST['phone'])
    obj = supporter.objects.get(phone_no = ph)
    obj.delete()
    return render(request,'supp/deleted.html',{"member":mem})


@login_required
def view_supp(request):
    mem = member.objects.get(user = request.user)
    if request.method == 'GET':
        supp = supporter.objects.all()
        context = {
            'supp': supp,
            'view':'details',
            "member":mem
        }
        return render(request, 'supp/edit_spp.html', context)
    if request.method == 'POST':
        value = request.POST['supp_name']
        print(value)
        value = value.split(',')
        ph = value[1]
        print(ph)
        na = value[0]
        print(value, ph, na)
        obj = supporter.objects.get(name=na, phone_no=ph)
        context = {
            'supp':obj,
            'view':'details',
            "member":mem
        }
    return render(request,'supp/detail.html',context)


@login_required
def view_don(request):
    mem = member.objects.get(user = request.user)
    supp = supporter.objects.get(phone_no = request.POST['phone'])
    dons = verified_donation.objects.filter(member = supp)
    values = []
    total=0
    for don in dons:
        values.append([don.rec_no,don.member.name, don.amount, don.date_donation, don.mode_donation, don.date_rec,don.migrated])
        total+=int(don.amount)
    context={
        'values' : values,
        'view'   : 'details',
        'total'  :  total,
        "member":mem
    }
    return render(request,'donation/don_added.html',context)


choices=[]


@login_required
def import_supp(request):
    mem = member.objects.get(user = request.user)
    global choices
    if request.method == 'POST':
        form = forms.Uploadfiles(request.POST, request.FILES)
        if form.is_valid():
            file_data = request.FILES['file']
            fs = FileSystemStorage()
            if fs.exists('temp.xlsx'):
                fs.delete('temp.xlsx')
            fs.save('temp.xlsx', file_data)
        mapping={'name':'0','age':'1','gender':'2','phone_no':'3','alt_phone_no':'4','email':'5','city':'6','ref':'7','pan_card':'8','is_constant':'9','amount':'10','adress':'11','is_sponsor':'12',"child_name":'13','is_one_time':'14','is_si':'15','si_date':'16','profession':'17'}
        import_worker(mapping)
        form=forms.Uploadfiles()
        return render(request, 'supp/import.html', {'form': form,"member":mem})
    else:
        form = forms.Uploadfiles()
        return render(request, 'supp/import.html', {'form':form,"member":mem})

def export_supporters(request):
    try:
        os.remove("supporters_export.xlsx")
    except:
        pass
    wb = Workbook()
    ws = wb.active
    ws.title = "Supporters"
    supp = supporter.objects.all()
    ws.cell(column = 1,row = 1).value = "Sr.No"
    ws.cell(column = 2,row = 1).value = "Name"
    ws.cell(column = 3,row = 1).value = "Age"
    ws.cell(column = 4,row = 1).value = "Gender"
    ws.cell(column = 5,row = 1).value = "Phone Number"
    ws.cell(column = 6,row = 1).value = "Alt Phone Number"
    ws.cell(column = 7,row = 1).value = "Email"
    ws.cell(column = 8,row = 1).value = "City"
    ws.cell(column = 9,row = 1).value = "Reference"
    ws.cell(column = 10,row = 1).value = "Pan Card"
    ws.cell(column = 11,row = 1).value = "Address"
    ws.cell(column = 12,row = 1).value = "Date Added"
    ws.cell(column = 13,row = 1).value = "Last Edited"
    ws.cell(column = 14,row = 1).value = "Is Constant"
    ws.cell(column = 15,row = 1).value = "Amount"
    ws.cell(column = 16,row = 1).value = "Is One Time"
    ws.cell(column = 17,row = 1).value = "Is Sponsor"
    ws.cell(column = 18,row = 1).value = "Childs Name"
    ws.cell(column = 19,row = 1).value = "Profession"
    ws.cell(column = 20,row = 1).value = "Is Resources"
    ws.cell(column = 21,row = 1).value = "Is SI"
    ws.cell(column = 22,row = 1).value = "SI Date"
    row_no = 2
    for entity in supp:
        ws.cell(column = 1,row = row_no).value = row_no
        ws.cell(column = 2,row = row_no).value = entity.name
        ws.cell(column = 3,row = row_no).value = entity.age
        ws.cell(column = 4,row = row_no).value = entity.gender
        ws.cell(column = 5,row = row_no).value = entity.phone_no
        ws.cell(column = 6,row = row_no).value = entity.alt_phone_no
        ws.cell(column = 7,row = row_no).value = entity.email_id
        ws.cell(column = 8,row = row_no).value = entity.city
        ws.cell(column = 9,row = row_no).value = entity.Reference
        ws.cell(column = 10,row = row_no).value = entity.pan_card
        ws.cell(column = 11,row = row_no).value = entity.address_a
        ws.cell(column = 12,row = row_no).value = entity.date_added
        ws.cell(column = 13,row = row_no).value = entity.date_edited
        ws.cell(column = 14,row = row_no).value = entity.is_constant
        ws.cell(column = 15,row = row_no).value = entity.amount
        ws.cell(column = 16,row = row_no).value = entity.is_one_time
        ws.cell(column = 17,row = row_no).value = entity.is_sponsor
        ws.cell(column = 18,row = row_no).value = entity.sponsee
        ws.cell(column = 19,row = row_no).value = entity.profession
        ws.cell(column = 20,row = row_no).value = entity.resources
        ws.cell(column = 21,row = row_no).value = entity.is_si
        ws.cell(column = 22,row = row_no).value = entity.si_date
        row_no+=1
    wb.save("supporters_export.xlsx")
    exp_file = open("supporters_export.xlsx","rb")
    return FileResponse(exp_file)


def import_worker(mapping):
    wb = load_workbook('media/temp.xlsx')
    print('inside to import worker')
    ws=wb['Main']
    rows = ws.rows
    supporter.objects.all().delete()
    for row in rows:
        try:
            phone = str(row[int(mapping['phone_no'])].value)
            name = (row[int(mapping['name'])].value)
            age = (row[int(mapping['age'])].value)
            gender = (row[int(mapping['gender'])].value)
            alt_phone_no = (row[int(mapping['alt_phone_no'])].value)
            email = (row[int(mapping['email'])].value)
            ref = (row[int(mapping['ref'])].value)
            city = (row[int(mapping['city'])].value)
            pan_card = (row[int(mapping['pan_card'])].value)
            is_cons = (row[int(mapping['is_constant'])].value)
            amount = (row[int(mapping['amount'])].value)
            addr = (row[int(mapping['adress'])].value)
            is_spons = (row[int(mapping['is_sponsor'])].value)
            child = (row[int(mapping['child_name'])].value)
            isonetime = (row[int(mapping['is_one_time'])].value)
            is_si = (row[int(mapping['is_si'])].value)
            si_date = (row[int(mapping['si_date'])].value)
            profession = (row[int(mapping['profession'])].value) 
            sup = supporter(name=name, age=age, gender=gender,
                         alt_phone_no=alt_phone_no,
                         email_id=email, city=city,
                         Reference=ref,address_a=addr,
                         phone_no=phone,pan_card = pan_card,
                         profession = profession
                         )
            if check_yes_no(is_cons):
                sup.is_constant = True
                try:
                    sup.amount = int(amount)
                except:
                    sup.amount = 0
            if check_yes_no(is_spons):
                sup.is_sponsor = True
                sup.sponsee = child
            if check_yes_no(isonetime):
                sup.is_one_time = True
            if check_yes_no(is_si):
                sup.is_si = True
                try:
                    sup.si_date = int(si_date)
                except:
                    sup.si_date = 0
            sup.save()
            print(name)
        except Exception as e:
            print('exceptionn',e)
                

def check_yes_no(value):
    try:
        if value.lower() == 'yes':
            return True
        else:
            return False
    except:
        return False