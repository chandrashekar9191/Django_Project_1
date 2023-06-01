from django import forms
from .models import Employee


class Employee_page(forms.ModelForm):

    class Meta:
        model=Employee
        fields=('fullName','emp_code','phone','position')
        
        labels={
            'fullName':'Full Name',
            'emp_code':'Emp_Code',
            'position':'Designation'
        }
    
    def __init__(self,*args,**kwargs):
        super(Employee_page,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label="select"
        