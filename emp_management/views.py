from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def home(request):
    isActive = True

    # to get data from website eg:input field data showing here
    if request.method == "POST":
        check = request.POST.get('check')
        print(check)

        if check is None: isActive=False
        else: isActive=True
    date=datetime.datetime.now()

    # dynamic data below  
    name = "LearnWithSishir"
    list_of_programs = [
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascals triangle'
    ]

    student = {
        'student_name':"Sishir",
        'student_college':"BVC",
        'student_city':"HYD" 
    }

    data = {
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }  
    # end of dynamic data

    return render(request,"home.html",data)

def about(request):
    return render(request,"about.html",{})

def services(request):
    return render(request,"services.html",{})