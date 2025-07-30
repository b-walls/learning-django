from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from myapp.forms import AttendanceForm
from .models import Menu

def home(request):
    return render(request, 'home.html')

def menu(request):
    items = Menu.objects.all()
    context = {'menu': items}
    return render(request, 'menu.html', context=context)

def about(request):
    about_content = {'about': "Based in Chicago, Illinois, Little Lemon is an amazing restaurant!!"}
    return render(request, "about.html", context=about_content)

def attendance_view(request):
    form = AttendanceForm()
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "attendance.html", context)