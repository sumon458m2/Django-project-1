from django.shortcuts import render
from.models import about
def portfulio(request):
    aboutdata=about.objects.all()
    context={
        'about':aboutdata
    }
    return render(request,'portfulio.html',context)