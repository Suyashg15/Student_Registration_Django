from django.shortcuts import render, redirect
from .models import stud
from .forms import StudForm,SForm

# Create your views here.
#For accessing the webpages
def show(request):
    return render(request,"home.html") #render is used to drawing(displaying) the webpage on the browser

def about(request):
    return render(request,'about.html') #renders the about.html page


def register(request):
    title="NEW STUDENT REGISTRATION"
    form=StudForm(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['s_name']
        clas=form.cleaned_data['s_class']
        addr=form.cleaned_data['s_addr']
        school=form.cleaned_data['s_school']
        mail=form.cleaned_data['s_email']
        email=stud.objects.filter(s_email=mail)#For avoiding repetitive registration of same student
        if len(email)>0:
            return render(request,'ack.html',{'title':"STUDENT ALREADY EXITS..TRY WITH OTHER EMAIL"})
        else:
            p=stud(s_name=name,s_class=clas,s_addr=addr,s_school=school,s_email=mail)
            p.save()
            return render(request,"ack.html",{"title":"REGISTERED SUCCESSFULLY"})

    context={
        "title":title,
        "form":form,
    }
    return render(request,"register.html",context)

def existing(request):
    title="ALL REGISTERED STUDENTS"
    queryset=stud.objects.all()#For displaying the database
    context={
        "title":title,
        "queryset":queryset,
    }
    return render(request,"existing.html",context)

def search(request):
    title="SEARCH STUDENTS"

    form=SForm(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['s_name']
        queryset=stud.objects.filter(s_name=name)#filtering or searching the name in stud
        if len(queryset)==0:#For returning error msg when data not found
            return render(request,'ack.html',{'title':'STUDENT DETAILS NOT FOUND....PLEASE ENTER CORRECT DATA'})

        context={
            'title':title,
            'queryset':queryset

        }
        return render(request,'existing.html',context)


    context={
        "title":title,
        'form':form,
    }
    return render(request,"search.html",context)


def dropout(request):
    title="DROPPING STUDENTS"

    form=SForm(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['s_name']
        queryset=stud.objects.filter(s_name=name).delete()#filtering or searching the name in stud
        return render(request,'ack.html',{'title':"STUDENT IS REMOVED FROM YOUR DATABASE"})


    context={
        "title":title,
        'form':form,
    }
    return render(request,"search.html",context)