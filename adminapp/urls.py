from django.urls.conf import path
from . import views

urlpatterns = [
    path('adminlogin/', views.fnlogin, name='adminlogin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customer/', views.fncustomer, name='customer'),
    path('fnuser/', views.fnuser, name='user'),
    path('newloan/', views.fnnewloan, name='newloan'),
    path('items/', views.fnitems, name='items'),
    path('itemgroup/', views.fnitemgroup, name='itemgroup'),
    path('interest/', views.fninterest, name='interest'),
    path('loanhistory/', views.loanhistory, name='loanhistory'),
]
