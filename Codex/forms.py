from django import forms

class TaskForm(forms.Form):
    name = forms.CharField()
    expense = forms.FloatField()
    category = forms.CharField()
    status = forms.CharField()
    description = forms.CharField()


class ProjectForm(forms.Form):
    name = forms.CharField()
    budget = forms.FloatField()
    description = forms.CharField()
    due_date = forms.DateField()