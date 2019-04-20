"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from expense.views import home_view
from expense.views import login
from expense.views import expense_detail_view
from expense.views import expense_create_view
from expense.views import expense_delete_view
from expense.views import expense_update_view
from expense.views import update_view
from expense.views import expense_orderby_title
from expense.views import expense_orderby_date
from expense.views import expense_orderby_ammount
from expense.views import filter_view_title
from expense.views import filter_view_ammount
urlpatterns = [
	path('',login,name='login'),
    path('admin/', admin.site.urls),
    path('showexpense/',expense_detail_view),
    path('home/',home_view),
    path('createexpense/',expense_create_view),
    path('deleteexpense/<id>',expense_delete_view),
    path('updateexpense/<id>',expense_update_view),
    path('update_view/',update_view),
    path('expense_orderby_title/',expense_orderby_title),
    path('expense_orderby_date/',expense_orderby_date),
    path('expense_orderby_ammount/',expense_orderby_ammount),
    path('filter_view_title/',filter_view_title),
    path('filter_view_ammount/',filter_view_ammount),
]

