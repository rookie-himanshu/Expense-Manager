from django.shortcuts import render
from .models import expense
from .form import expenseform
from django.db.models import Sum
#for login
def login(request,*args,**kwargs):
	
	
	return render(request,"login.html",{})
#after login, home will be rendered
def home_view(request,*args,**kwargs):
	
	
	return render(request,"home.html",{})

#for creation of new expense record
def expense_create_view(request):
	form=expenseform(request.POST or None)
	if form.is_valid():
		form.save()
		form=expenseform()

	context={
	"form": form
	}

	return render(request,"expense/create.html",context)

#for displaying all Expenses and total expense Sum
def expense_detail_view(request):
	obj=expense.objects.all()
	sum=expense.objects.aggregate(Sum('ammount'))
	context={
	"obje":obj,
	"sum":sum
	}
	return render(request,"expense/details.html",context)

#for Deletion of old Expense
def expense_delete_view(request,id):
	
	expense.objects.filter(id=id).delete()
	sum=expense.objects.aggregate(Sum('ammount'))
	obj=expense.objects.all()
	context={
	"obje":obj,
	"sum":sum
	}
	return render(request,"expense/details.html",context)
#following two, will be used for updating existing expense
def expense_update_view(request,id):
	obj=expense.objects.get(id=id)
	context={
	"obje":obj
	}
	return render(request,"expense/pdetails.html",context)


def update_view(request):
	id=request.GET['id']
	title=request.GET['title']
	description=request.GET['description']
	ammount=request.GET['ammount']
	obj = expense.objects.get(id=id)
	obj.title = title
	obj.description = description
	obj.ammount = ammount
	obj.save()
	sum=expense.objects.aggregate(Sum('ammount'))
	obj=expense.objects.all()
	context={
	"obje":obj,
	"sum":sum
	}
	return render(request,"expense/details.html",context)


#used for displaying Expenses in sorted order according to title
def expense_orderby_title(request):
	obj=expense.objects.all().order_by('title')
	sum=expense.objects.aggregate(Sum('ammount'))
	context={	
	"obje":obj,
	"sum":sum
	}
	return render(request,"expense/details.html",context)

#used for displaying Expenses in sorted order according to Date of creation
def expense_orderby_date(request):
	obj=expense.objects.all().order_by('date')
	sum=expense.objects.aggregate(Sum('ammount'))
	context={	
	"obje":obj,
	"sum":sum
	}
	return render(request,"expense/details.html",context)


#used for displaying Expenses in sorted order according to ammount
def expense_orderby_ammount(request):
	obj=expense.objects.all().order_by('ammount')
	sum=expense.objects.aggregate(Sum('ammount'))
	context={	
	"obje":obj,
	"sum":sum
	}
	return render(request,"expense/details.html",context)



#used for displaying filtered Expenses for a given title
def filter_view_title(request):
	title=request.GET['title']
	obj=expense.objects.filter(title=title)
	sum=expense.objects.aggregate(Sum('ammount'))
	context={	
	"obje":obj,
	"sum":sum
	}
	return render(request,"expense/details.html",context)


#used for displaying all the  Expenses ranging between starting and ending value of ammount
def filter_view_ammount(request):
	start=request.GET['start']
	end=request.GET['end']
	obj=expense.objects.filter(ammount__range=(start, end))
	sum=expense.objects.aggregate(Sum('ammount'))
	context={	
	"obje":obj,
	"sum":sum
	}
	return render(request,"expense/details.html",context)

