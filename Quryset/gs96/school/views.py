from django.shortcuts import render
from .models import student
from .models import teacher
# Create your views here.

def home(request):
    student_data  = student.objects.all()

    #student_data  = student.objects.filter( roll = 104)

    #student_data  = student.objects.exclude( roll = 103)

    #student_data  = student.objects.order_by('id')

    #student_data  = student.objects.order_by('id').reverse() [: 3]

    #student_data  = student.objects.values('id','name')

   #student_data  = student.objects.values('pass_date','roll')

    #student_data  = student.objects.filter( roll = 105) & student.objects.filter( id = 4)

    #student_data  = student.objects.filter( name = 'guru') & student.objects.filter( city = 'assam')

    # student_data1  = student.objects.values_list('id','name', named=True)

    # student_data2  = teacher.objects.values_list('id','name', named=True )

    # student_data = student_data2.union(student_data1)
    
    # student_data1  = student.objects.values_list('id','name', named=True)

    # student_data2  = teacher.objects.values_list('id','name', named=True )

    # student_data = student_data2.intersection(student_data1)
    
    # student_data1  = student.objects.values_list('id','name', named=True)

    # student_data2  = teacher.objects.values_list('id','name', named=True )

    # student_data = student_data1.difference(student_data2)

    #teacher_data = teacher.objects.union()

    #print("queryset",student_data.query) # it will give the sql query 

    return render(request, 'school/home.html',
                  {'stud':student_data})

