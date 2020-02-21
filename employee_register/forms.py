from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ('fullname', 'email', 'content', 'position')
		labels  = {
					'position': 'Position',
					'fullname': 'Full Name',
					'email'   : 'Email',
					'content' : 'Content'
				  }  

	def __init__(self, *args, **kwargs):
		super(EmployeeForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = False
		self.fields['position'].empty_label = "Select"   

