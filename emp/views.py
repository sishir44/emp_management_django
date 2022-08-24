from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp, Testimonial
from .form import FeedbackForm, EmpForm

# Create your views here.

def emp_home(request):
    emps = Emp.objects.all()
    return render(request,'emp/home.html',{'emps':emps})


def add_emp(request):
    if request.method == 'POST':

        # data fetch
        emp_name = request.POST.get("emp_name")
        emp_id1 = request.POST.get("emp_id1")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")
       
        # create model object and set the data
        e = Emp()
        e.name = emp_name
        e.emp_id = emp_id1
        e.phone = emp_phone
        e.address = emp_address

        if emp_working is None: e.working = False
        else: e.working = True

        e.department = emp_department

        # save the object
        e.save()
        return redirect("/emp/home/")
    #from Feedabck form.py
    form = EmpForm()  

    return render(request,'emp/add_emp.html', {'form':form})


def delete_emp(request,emp_id):
    emp = Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect('/emp/home')

def update_emp(request,emp_id):
    emp = Emp.objects.get(pk=emp_id)
    return render(request,'emp/update_emp.html',{'emp':emp})

def do_update_emp(request, emp_id):
    if request.method == 'POST':
        emp_name = request.POST.get("emp_name")
        emp_id1_temp = request.POST.get("emp_id1")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        e = Emp.objects.get(pk=emp_id)

        e.name = emp_name
        e.emp_id = emp_id1_temp
        e.phone = emp_phone
        e.address = emp_address

        if emp_working is None: e.working = False
        else: e.working = True

        e.department = emp_department

        e.save()
    return redirect('/emp/home/')

   
def testimonials(request):
    testi = Testimonial.objects.all()
    
    return render(request,'emp/testimonials.html',{'testi':testi})

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            print("data saved")
        else:
            return render(request, 'emp/feedback.html', {'form':form})
    else:
        form = FeedbackForm()
        return render(request, 'emp/feedback.html', {'form':form})