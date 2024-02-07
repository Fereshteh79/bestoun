from django.urls import path

from . import views

urlspatterns = [
    path('^submit/expense/$', views.submit_expense, name='submit_expense')

]
