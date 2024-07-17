from django.shortcuts import render, redirect
from web.models import Student
from django.contrib import messages

# Create your views here.

def home(requests):
    return render(requests, 'web/index.html')
def profile(requests, profile):
    return render(requests, 'web/profile.html', {'profile':'favour'})
def student(requests):
    all_students = Student.objects.all()
    context = {'data': all_students}

    return render(requests, 'web/students.html', context)
def newstudent(requests):
    if requests.method == "POST":
        # name = requests.POST["named"]
        name = requests.POST.get("name")
        reg_number = requests.POST.get("Registration")
        age = requests.POST.get("age")
        cgpa = requests.POST.get("cgpa")
        dj = requests.POST.get("datejoined")
        # print(name, reg_number, age, cgpa, dj)
        if not name or not reg_number or not age or not cgpa or not dj:
            # print("something is missing")
            messages.error(requests, "All fields are required")
            return redirect(newstudent)

        new_student = Student.objects.create(name = name,
        reg_number = reg_number,
        age = age,
        cgpa = cgpa)
        new_student.save()
        messages.success(requests, "created successfully")
        return redirect(home)
    # print(requests.method)
    return render(requests, 'web/newstudent.html')