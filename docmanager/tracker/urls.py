from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('add-employee/', views.add_employee, name='add_employee'),
    path('add-document/', views.add_document, name='add_document'),
    path('employee/edit/<int:pk>/', views.edit_employee, name="edit_employee"),
    path('employee/delete/<int:pk>/', views.delete_employee, name="delete_employee"),
    path('document/edit/<int:pk>/', views.edit_document, name="edit_document"),
    path('document/delete/<int:pk>/', views.delete_document, name="delete_document"),
]