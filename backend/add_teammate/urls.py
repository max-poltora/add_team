from django.urls import path
from . import views
from add_teammate.views import TableView

urlpatterns = [
    path('', views.main, name='add_teammate_main'),
    path('table/', TableView.as_view()),
]
