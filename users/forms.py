from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import Manager,Teacher,Student,Attendance



class_attendance = (
    ('Present','נוכח'),
    ('Absent','לא נוכח'),
)

class AttendanceForm(forms.Form):
    mark_attendance = forms.ChoiceField(widget=forms.RadioSelect, choices=class_attendance)
