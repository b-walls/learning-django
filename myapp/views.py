from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from myapp.forms import AttendanceForm
from .models import Menu

def home(request):
    return HttpResponse("Welcome to Little Lemon.")

def hello(request):
    return HttpResponse("Hello World!")

def menu(request, category):
    items = Menu.objects.filter(category_id=category)
    html = f"<h1>{category}(s)</h1>"

    for item in items:
        html += f"<h2>{item.menu_item} : ${item.price}</h2>"

    return HttpResponse(html)

def attendance_view(request):
    form = AttendanceForm()
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "home.html", context)