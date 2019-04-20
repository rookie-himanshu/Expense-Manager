#this form is used for creation of Expense object

from django import forms
from .models import expense
class expenseform(forms.ModelForm):
	class Meta:
		model=expense
		fields=[
		'title',
		'description',
		'ammount'

		]