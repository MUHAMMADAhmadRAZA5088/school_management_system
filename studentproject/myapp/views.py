import csv
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Student,Class,Section
from django.http import HttpResponse
# Create your views here.

def login(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')  # Using 'username' instead of 'email'
        password = request.POST.get('password')
        # Authenticate user based on username and password
        user = authenticate(request, username=name, password=password)
        if user is not None:
            if user.is_superuser:  # Check if the user is a superuser
                auth_login(request, user)  # Use 'auth_login' to avoid conflict
                # Redirect to dashboard or any page you like
                return redirect('dashboard')
            else:
                messages.success(request, 'password & name are not correct')
                return redirect('login')
        else:
            messages.success(request, 'password & name are not correct')
            return redirect('login')  # Reload the login page with error
    else:
        return render(request, 'login.html')
  
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def student_class(request):
    data = []
    classes = Class.objects.all()
    if classes:
        for i in range(len(classes)):
            obj ={}
            obj[f"total_student"] = len(Student.objects.filter(student_class= str(classes[i].class_name)))

            if len(str(obj[f"total_student"])) == 1: 
               obj[f"total_student"] = '0' + str(obj[f"total_student"])
            else:
                obj[f"total_student"] = str(obj[f"total_student"])
            
            obj["class_name"] =  classes[i].class_name
            obj["count"] = i%2
            data.append(obj)
        
        return render(request, 'student_class.html', {"class_data" : data})

def student_view(request, slug):

    section_dropdown = Section.objects.all()
    school_class = Student.objects.filter(student_class= str(slug))
    return render(request, 'student_view.html',{'students':school_class,"sections":section_dropdown,
                                                "class_name":slug})

def add_student(request):
    class_dropdown = Class.objects.all()
    section_dropdown = Section.objects.all()
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        father_name = request.POST.get('father_name')
        b_form_id = request.POST.get('student_bform')
        father_id_card = request.POST.get('father_id_card')
        phone_number = request.POST.get('phone_number')
        section = request.POST.get('section')
        student_class = request.POST.get('class')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        picture = request.FILES.get('picture')
        
        student = Student(
            student_name=student_name,
            father_name=father_name,
            b_form_id=b_form_id,
            father_id_card=father_id_card,
            phone_number=phone_number,
            section=section,
            student_class=student_class,
            dob=dob,
            picture=picture,
            address=address
        )
        student.save()
        messages.success(request, 'Student Add successfully')
        return redirect('add_student')

    return render(request, 'add_student.html',{"Classes":class_dropdown,"sections":section_dropdown})

def update_view(request, slug):
    
    student = get_object_or_404(Student, id=slug)
    import pdb;pdb.set_trace()
    print(student)

def delete_student(request,slug):
    student = get_object_or_404(Student, id=slug)
    student.delete()
    messages.success(request, 'Delete student successfully')
    return render (request, 'student_view.html')

   


def student_profile(request, slug):
    student = get_object_or_404(Student, id=slug)
    return render(request, 'student_profile.html',{'student' : student})

def section_add(request):
    db_section = Section.objects.all()

    if request.method == 'POST':
        section = request.POST.get('add_scetion')
        
        if section :
            section = Section(
                section = section
            )
            
            section.save()
            messages.success(request, 'Section Add successfully')
            # return redirect('section_add')
    return render(request, 'custom_section_add.html',{"sections": db_section})

def class_add(request):
    db_Class = Class.objects.all()
    if request.method == 'POST':
        class_add = request.POST.get('add_class')
        
        if class_add :
            class_data = Class(
                class_name = class_add
            )
            
            class_data.save()
            messages.success(request, 'Class Add successfully')
            return redirect('class_add')
    return render(request, 'custom_class_add.html',{"Classes": db_Class})



