from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Document
from .forms import EmployeeForm, DocumentForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    employees = Employee.objects.all()

    query = request.GET.get('query')
    if query:
        documents = Document.objects.filter(employee__name__icontains=query)
    else:
        documents = Document.objects.all()

    context = {
        'employees':employees,
        'documents':documents,
        'query':query,
    }
    return render(request, 'tracker/dashboard.html', context)

def add_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'tracker/add_employee.html', {'form':form})


def add_document(request):
    form = DocumentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'tracker/add_document.html', {'form':form})


def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form =EmployeeForm(request.POST or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect("dashboard")
    return render(request, "tracker/add_employee.html", {"form":form})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect("dashboard")


def edit_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    form = DocumentForm(request.POST or None, request.FILES or None, instance=document)

    if form.is_valid():
        form.save()
        return redirect("dashboard")
    return render(request, "tracker/add_document.html", {"form":form})


def delete_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    document.delete()
    return redirect("dashboard")

