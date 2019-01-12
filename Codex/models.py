from django.db import models
from datetime import *


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    budget = models.DecimalField(max_digits=8, decimal_places=2)
    due_date = models.DateField()

    # Return Remaining Budget
    def budgetRemaining(self):
        expenses = Task.objects.filter(project=self)
        amount = 0
        for expense in expenses:
            amount += expense.expense

        return self.budget - amount

    # Return the total number of tasks related to a project
    def totalTasks(self):
        return Task.objects.filter(project=self).count()

    # Retrun the total number of finished tasks
    def finishedTasks(self):
        return Task.objects.filter(project=self).filter(status="Finished").count()

    # Return progress precentage
    def projectProgress(self):
        complete = self.finishedTasks()
        total = self.totalTasks()
        if not total == 0:
            return int((complete / total) * 100)
        return 0

    # Return remainig days to the due date
    def due(self):
        today = date.today()
        due = self.due_date - today
        return due.days


class Task(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='tasks')
    description = models.TextField()
    name = models.CharField(max_length=50)
    expense = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
