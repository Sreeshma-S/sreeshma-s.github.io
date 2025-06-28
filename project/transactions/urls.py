from django.urls import path
from transactions.views import transactions_list
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('transactions_list/', transactions_list, name='transactions_list'),
]
