from django.shortcuts import render,redirect
from ForeignApp.models import Course,Student

def home(request):
    return render(request,'home.html')

def addCourse(request):
    return render(request,'add_course.html')

def saveCourse(request):
    if request.method=="POST":
        name=request.POST['c_name']
        fee=request.POST['c_fee']
        course=Course(course_name=name,fee=fee)
        course.save()
        return redirect('home')

def addStudent(request):
    course=Course.objects.all()
    return render(request,'add_student.html',{'course':course})

def saveStudent(request):
    if request.method=="POST":
        name=request.POST['s_name']
        addr=request.POST['s_add']
        age=request.POST['s_age']
        date=request.POST['jod']
        cid=request.POST['course']
        course=Course.objects.get(id=cid)
        student=Student(course=course,student_name=name,student_address=addr,student_age=age,joining_date=date)
        student.save()
        return redirect('addStudent')
    
def displayStudent(request):
    stud=Student.objects.all()
    return render(request,'displayStud.html',{'stud':stud})

def edit(request,pk):
    course=Course.objects.all()
    stud=Student.objects.get(id=pk)
    return render(request,'edit.html',{'stud':stud,'course':course})

def updateStudent(request,pk):
    if request.method=="POST":
        student=Student.objects.get(id=pk)
        student.student_name=request.POST['s_name']
        student.student_address=request.POST['s_add']
        student.student_age=request.POST['s_age']
        student.joining_date=request.POST['jod']
        courseid=request.POST['course']
        student.course=Course.objects.get(id=courseid)
        student.save()
        return redirect('displayStudent')
    
def delete(request,pk):
    stud=Student.objects.get(id=pk)
    stud.delete()
    return redirect('displayStudent')
# Create your views here.