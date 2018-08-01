from django import forms  
from student.models import Employee  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  


class sendmail(forms.Form):
    to=forms.CharField(max_length=50)
    subject=forms.CharField(max_length=300)
    body=forms.CharField(max_length=500)

