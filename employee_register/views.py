from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm
# Create your views here.


def employee_form(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        
        if form.is_valid():
            form.save()

            return redirect('/register/employee_list')
    else:
        form = EmployeeForm()
    return render(request, "employee_register/employee_form.html", {'form': form})   


def employee_Update(request, id):

    employee = Employee.objects.get(pk=id)
    form = EmployeeForm(instance=employee)
    
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        
        if form.is_valid():
            form.save()

            return redirect('/register/employee_list')

    context = {'form':form}
    return render(request, "employee_register/employee_form.html", context)


def employee_list(request):
    emp = Employee.objects.all()
    context = {'emp': emp}
    return render(request, 'employee_register/employee_list.html', context)

    
def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/register/employee_list')


def employee_delete_all(request):
   # if len(employee) == 8:

    Employee.objects.all().delete()

    return render(request, 'employee_register/employee_list.html')
