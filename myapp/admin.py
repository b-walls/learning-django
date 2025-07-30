from django.contrib import admin
from .models import Menu, MenuCategory, Attendance, Reservation

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(Attendance)
admin.site.register(Reservation)
