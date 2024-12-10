from django.shortcuts import render
# Create your views here.
# creating range
#my_dict={"time":range(5)}
#std_data={"std_info":{'Arpit': 9.0,'Aman': 8,'Kunjan': 8.0},'time':range(5)}
students = [
        {'name': 'John', 'course': 'Math', 'cgpa': 3.5, 'age': 20},
        {'name': 'Jane', 'course': 'Science', 'cgpa': 3.8, 'age': 21},
        {'name': 'Doe', 'course': 'History', 'cgpa': 3.2, 'age': 22},
    ]
context = {'students': students}
def index(request):
    return render(request,'first_app/index.html',context)