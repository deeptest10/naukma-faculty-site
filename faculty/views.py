from django.shortcuts import render, get_object_or_404
from .models import Department, Program, FacultyInfo


def home(request):
    faculty = FacultyInfo.objects.first()
    return render(request, "faculty/home.html", {"faculty": faculty})


def program_list(request):
    programs = Program.objects.all()
    return render(request, "faculty/program_list.html", {"programs": programs})


def program_detail(request, id):
    program = get_object_or_404(Program, id=id)
    return render(request, "faculty/program_detail.html", {"program": program})


def department_list(request):
    departments = Department.objects.all()
    return render(
        request,
        "faculty/department_list.html",
        {"departments": departments},
    )


def department_detail(request, id):
    department = get_object_or_404(Department, id=id)
    return render(
        request,
        "faculty/department_detail.html",
        {"department": department},
    )