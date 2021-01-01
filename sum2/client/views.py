from django.shortcuts import render
from.models import about
def clientus(request):
    aboutdata=about.objects.all()
    context={
        'about':aboutdata
    }
    return render(request,'client.html',context)