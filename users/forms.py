from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import Manager,Teacher,Student,Attendance



class_attendance = (
    ('Present','Present'),
    ('Absent','Absent'),
)

class AttendanceForm(forms.Form):
    mark_attendance = forms.ChoiceField(widget=forms.RadioSelect, choices=class_attendance)
