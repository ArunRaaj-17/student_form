from django.shortcuts import render,redirect
from .models import *
from .forms import *

def home(request):
    return render(request,'home.html')

def addstudents(request):
    context={
        'form':StudentForm
    }
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=StudentForm()
        
        return redirect('/allstudents/')

    return render(request,'addstudents.html',context)

def allstudents(request):
    context={
        'all_student':Student.objects.all()
    }
    return render(request,'allstudents.html',context)

def delete_student(request,id):
    select_student=Student.objects.get(id=id)
    select_student.delete()
    return redirect('/allstudents/')

def update_student(request,id):
    select_student=Student.objects.get(id=id)
    context={
       'form':StudentForm(instance=select_student)
    }
    if request.method =='POST':
        form=StudentForm(request.POST,instance=select_student)
        if form.is_valid:
            form.save()
        return redirect('/allstudents/')
        
    
    return render(request,'addstudents.html',context)