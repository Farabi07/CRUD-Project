from django.shortcuts import render
from .forms import StudentForm
from .models import Student


# Create your views here.

def index(request):
    student_list = Student.objects.order_by('pk')
    diction = {'title': 'Index', 'student_list': student_list}
    return render(request, 'myapp/index.html', context=diction)


def student_form(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction = {'title': 'Student Form', 'student_form': form}
    return render(request, 'myapp/student_form.html', context=diction)


def student_info(request, student_id):
    student_info = Student.objects.get(pk=student_id)
    diction = {'student_info': student_info}
    return render(request, 'myapp/student_info.html', context=diction)

def student_update(request,student_id):
    student_info=Student.objects.get(pk=student_id)
    form=StudentForm(instance=student_info)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student_info)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction={'student_update':form}
    return render(request,'myapp/student_update.html',context=diction)


def student_delete(request,student_id):
    student_list = Student.objects.get(pk=student_id).delete()
    diction = {'delete_message':'DELETED'}
    return render(request, 'myapp/student_delete.html', context=diction)
