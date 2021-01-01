from django.shortcuts import render
from.models import section
def home(request):
    sectiondata=section.objects.all()
    context={
        'section':sectiondata
    }
    return render(request,'index.html',context)