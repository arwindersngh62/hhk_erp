from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView
from .forms import add_exp
from usersreg.models import member
from .models import expense,settled
from django.contrib.auth.decorators import login_required
# Create your views here.
def add_exp_view(request):
	form = add_exp()
	return render(request,'exptemp/add_exp.html',{'form':form})

# to do fix resubmitting problem by using redirect
def generate_exp(request):
#mem = member.objects.get(user = request.use
	formexp = add_exp(request.POST)
	newform = formexp.save(commit = False)
	newform.expense_date = request.POST["exp_date"]
	print("Saving Form")
	newform.save()
	return redirect('exptemp:generate_exp')
    #print(formexp.is_valid())
    #print(bool(request.POST["exp_date"]))
   	#formexp.save()
    # if form.is_valid():
    # 	form.save()
    # 	print('form saved')
    # else:
    # 	print(form.errors)

def success(request):
	return render(request,'exptemp/gen_exp.html')
def	appr_success(request):
	return render(request,'exptemp/exp_success.html')
@login_required
def settle_exp(request):
	expenses = expense.objects.filter(is_settled=False)
	#print(expenses)
	return render(request,'exptemp/approve_exp.html',{'expenses':expenses})
@login_required
def view_old(request):
	return render(request,'users/index.html')
@login_required
def detail_exp(request,key_id):
	expense_item = expense.objects.get(reimb_id=key_id)
	return render(request,'exptemp/detailexp.html',{'expense':expense_item})

def settle_exp_form(request):
	#print(request.method)
	data = []
	total = 0
	for i in request.POST:
		if 'expense' in i:
			data.append(expense.objects.get(reimb_id=int(request.POST[i])))
	for datum in data:
		total += int(datum.amount)
	return render(request,'exptemp/settleexp.html',{'expenses':data,'total':total})

def settled_view(request):
	#print(request.POST['payment_date'])
	mem = member.objects.get(user = request.user)
	settlement = settled(settled_by = mem, payment_date = request.POST['payment_date'],amount_approved = request.POST['amount_appr'],settled_comments = request.POST['settle_remarks'])
	settlement.save()
	exp_ids = []
	print(request.POST.keys())
	for item in request.POST.keys():
		if 'id_exp_head' in item:
			exp_ids.append(item.split('-')[1])
	print(exp_ids)
	for exp_id in exp_ids:
		expense_settle = expense.objects.get(reimb_id = exp_id)
		expense_settle.expense_head = request.POST['id_exp_head-'+str(exp_id)]
		expense_settle.category = request.POST['id_exp_subhead-'+str(exp_id)]
		expense_settle.sub_categroy = request.POST['id_expense_product-'+str(exp_id)]
		expense_settle.is_settled = True
		expense_settle.exp = settlement
		expense_settle.save() 
	return redirect('exptemp:appr_success')