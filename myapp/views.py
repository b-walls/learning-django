from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from myapp.forms import AttendanceForm
from .models import Menu

def home(request):
    return HttpResponse("Welcome to Little Lemon.")

def hello(request):
    return HttpResponse("Hello World!")

def menu_by_category(request, category):
    items = Menu.objects.filter(category_id=category)
    html = f"<h1>{category}(s)</h1>"

    for item in items:
        html += f"<h2>{item.menu_item} : ${item.price}</h2>"

    return HttpResponse(html)

def menu(request):
    items = Menu.objects.all()
    context = {'menu': items}
    return render(request, 'menu.html', context=context)
    

def attendance_view(request):
    form = AttendanceForm()
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "home.html", context)

def about(request):
    about_content = {'about': "Based in Chicago, Illinois, Little Lemon is an amazing restaurant!!"}
    return render(request, "about.html", context=about_content)