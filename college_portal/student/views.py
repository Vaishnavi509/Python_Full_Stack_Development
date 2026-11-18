from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    data={
    'name':"vaishu",
    'age':"20",
    'department':"bca",
    }
    marks=[100,90,80]
    return render(request,'home.html',{'data':data,'marks':marks})
def about(request):
      return render(request,'about.html')
def contact(request):
       return render(request,'contact.html')
