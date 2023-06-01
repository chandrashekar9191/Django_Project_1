from django.shortcuts import render,redirect
from .forms import Employee_page
from .models import Employee

# Create your views here.

def employee_list(request):
    context={'employee_list':Employee.objects.all()}
    return render(request,"employee_register/employee_list.html",context)
def employee_form(request,id=0):
    if request.method=="GET":
        if id==0:
            form=Employee_page()
        else:
            employee=Employee.objects.get(pk=id)
            form=Employee_page(instance=employee)
        return render(request,"employee_register/employee_form.html",{'form':form})
    else:
        if id ==0:
            form=Employee_page(request.POST)
        else:
            employee=Employee.objects.get(pk=id)
            form=Employee_page(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')
def employee_delete(request,id):
    employee=Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
