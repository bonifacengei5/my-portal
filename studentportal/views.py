from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages


def home(request):
    return render(request, 'index.html')


def add_student(request):
    if request.method == "POST":
        s_name = request.POST.get("s-name")
        s_gender = request.POST.get("s-gender")
        s_course = request.POST.get("s-course")

        context = {
            "s_name": s_name,
            "s_Email": s_gender,
            "S_age": s_course,

            "success": "Successful registration"
        }

        query = Student(name=s_name, gender=s_gender,
                        course=s_course)
        query.save()

    return render(request, 'add-student.html')


def student(request):
    add_students = Student.objects.all()
    context = {"all_students": add_students}

    return render(request, 'student.html', context)
