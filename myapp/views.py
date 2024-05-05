from django.shortcuts import render
import random
from myapp.data import lovecal, check



# Create your views here.

def home(request):
    return render(request,'home.html')

def action(request):

    if request.method == 'POST':
        name = request.POST.get('n1')
        lover = request.POST.get('n2')
        a = lovecal(name,lover)
        b = check(a)
        result = b[0]
        word = b[1]

        return render(request,'home.html',{'name':name,'lover':lover,'result':result,'word':word})





