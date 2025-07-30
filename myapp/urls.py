from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('hello/', views.hello),
    path('menu/<int:category>', views.menu),
    path('attendance/', views.attendance_view)
]