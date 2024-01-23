from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView, DeleteView, CreateView

from .models import Bot,Add,Web,Papular,Expert,Exp,Aexp,Cour,Instruct,Team,Courses
from .forms import ContactForms
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    adds = Add.objects.all()
    webs = Web.objects.all()
    papulars = Courses.objects.all()
    print("Papulars -->", papulars)
    experts = Expert.objects.all()
    exps = Exp.objects.all()
    context = {
        "adds":adds,
        "webs":webs,
        "papulars":papulars,
        "experts":experts,
        "exps":exps
    }
    return render(request,"index.html", context=context)

def courses(request):
    cours = Cour.objects.all()
    instructs = Instruct.objects.all()
    context = {
        "cours": cours,
        "instructs": instructs
    }
    return render(request,"courses.html",context=context)

class CoursesUpdateView(UpdateView):
    model = Courses
    fields = ('name', 'cost','tutor','numPupils','number')
    template_name = 'coursesEdit.html'



class CoursesDeleteView(DeleteView):
    model = Courses
    template_name = 'coursesDelete.html'
    success = reverse_lazy('index')

class CourseCreateView(CreateView):
    model = Courses
    template_name = "courseCreate.html"
    fields = ("name","cost","slug", "tutor", "time", "numPupils", "number", "img" )

def courseDetail(request, course):
    course = get_object_or_404(Courses,slug=course)
    context ={
        "course":course
    }
    return render(request,"courseDetail.html",context=context)

def A404(request):
    return render(request,"404.html",context={})

def about(request):
    aexps = Aexp.objects.all()
    context = {
        "aexps": aexps
    }
    return render(request,"about.html",context=context)

def testimonial(request):
    return render(request,"testimonial.html",context={})

def contact(request):
    contact = ContactForms(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>HABAR YUBORILDI  !!! <h2/> ")
    context = {
        "contact":contact
    }
    return render(request,"contact.html",context=context)

def team(request):
    teams = Team.objects.all()
    contxet = {
        "teams":teams
    }
    return render(request,"team.html",context=contxet)

class TeamUpdateView(UpdateView):
    model = Team
    fields = ('name', 'bio')
    template_name = 'teamsEdit.html'

class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'teamsDelete.html'
    success = reverse_lazy('team')

def teamsDetail(request, course):
    teams = get_object_or_404(Team,slug=course)
    context ={
        "teams":teams
    }
    return render(request,"teamDetail.html",context=context)

def addsdetailview(request,id):
    try:
        adds=Add.objects.get(id=id)
        context = {
            "adds":adds
        }
    except adds.DoesNotExist:
        raise Http404("No adds found")
    return render(request,"adds_detail.html",context=context)


def websdetailview(request,id):
    try:
        webs=Web.objects.get(id=id)
        print("Maluotlar = ", webs)
        context = {
            "webs":webs
        }
    except webs.DoesNotExist:
        raise Http404("No webs found")
    return render(request,"webs_detail.html",context=context)

def papularsdetailview(request,id):
    try:
        papulars=Papular.objects.get(id=id)
        context = {
            "papulars":papulars
        }
    except papulars.DoesNotExist:
        raise Http404("No papulars found")
    return render(request,"papulars_detail.html",context=context)


def expertsdetailview(request,id):
    try:
        experts=Expert.objects.get(id=id)
        context = {
            "experts":experts
        }
    except experts.DoesNotExist:
        raise Http404("No experts found")
    return render(request,"experts_detail.html",context=context)


def expsdetailview(request,id):
    try:
        exps=Exp.objects.get(id=id)
        context = {
            "exps":exps
        }
    except exps.DoesNotExist:
        raise Http404("No exps found")
    return render(request,"exps_detail.html",context=context)



def instructsdetailview(request,id):
    try:
        instructs=Instruct.objects.get(id=id)
        context = {
            "instructs":instructs
        }
    except instructs.DoesNotExist:
        raise Http404("No instructs found")
    return render(request,"instructs_detail.html",context=context)

def coursdetailview(request,id):
    try:
        cours=Cour.objects.get(id=id)
        context = {
            "cours":cours
        }
    except cours.DoesNotExist:
        raise Http404("No cours found")
    return render(request,"cours_detail.html",context=context)

def aexpsdetailview(request,id):
    try:
        aexps=Aexp.objects.get(id=id)
        context = {
            "aexps":aexps
        }
    except aexps.DoesNotExist:
        raise Http404("No aexps found")
    return render(request,"aexps_detail.html",context=context)

def teamsdetailview(request,id):
    try:
        teams=Aexp.objects.get(id=id)
        context = {
            "teams":teams
        }
    except teams.DoesNotExist:
        raise Http404("No teams found")
    return render(request,"teams_detail.html",context=context)




























































































































































