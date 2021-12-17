from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ("name", "user_id", "password","phone_number","school")

#class AttendanceForm(forms.Form):
#    mark_attendance = forms.ChoiceField(widget=forms.RadioSelect, choices=class_attendance)
