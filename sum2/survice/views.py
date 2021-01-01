from django.shortcuts import render
from.models import survice
def surv(request):
    survicedata=survice.objects.all()
    context={
        'survice':survicedata
    } 

    return render(request,'section.html',context)