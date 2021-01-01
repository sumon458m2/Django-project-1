from django.shortcuts import render
from.models import children,child,testmonial,team
def childus(request):
    childrendata=children.objects.all()
    childdata=child.objects.all()
    testmonialdata=testmonial.objects.all()
    teamdata=team.objects.all()
    context={
        'children':childrendata,
        'child':childdata,
        'testmonial':testmonialdata,
        'team':teamdata,
    }
    return render(request,'index.html',context)