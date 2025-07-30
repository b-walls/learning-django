from django import forms
from .models import Attendance

SHIFTS = (
    ("1", "Breakfast"),
    ("2", "Lunch"),
    ("3", "Dinner")
)

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

