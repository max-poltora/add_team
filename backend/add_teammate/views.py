# Tables tutorial: https://django-tables2.readthedocs.io/en/latest/pages/tutorial.html
# Django Forms - Save Form Data to Database with Model Forms: https://www.youtube.com/watch?v=6aQoW0TRXBk
from django.shortcuts import render, redirect
from django_tables2 import SingleTableView

from .forms import InputForm
from .models import Person
from .tables import Table

def main(request):
    form = InputForm()
    table = Table(Person.objects.all())
    if request.POST:
        form = InputForm(request.POST)
        if form.is_valid():    
            form.save()
        return redirect(main)
    return render(request, 'add_teammate/main.html', {'form': form, 'table': table})

class TableView(SingleTableView):
    model = Person
    table_class = Table
    template_name = 'add_teammate/table.html'

