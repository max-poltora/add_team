import django_tables2 as tables
from .models import Person

class Table(tables.Table):
    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
        fields = ('first_name', 'last_name', 'joined_date',)