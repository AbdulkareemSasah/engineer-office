from django.http import Http404
from django.shortcuts import render, get_list_or_404
from django.utils.translation import get_language
from .models import Catagury,Article,Keyword,Order,EmailList,Project
from .forms import OrderForm,EmailListForm


##
# DEFAULT CATAGURY
# *** SLIDER
# *** SERVICE
# *** ABOUT
# *** ADVANTAGE
# *** TYPE OF PROJECTS
# *** ##

def thome(request):
    cataguries = Catagury.objects.filter(active=True)
    sliders= Article.objects.filter(active=True,catagury__catagury="slider")
    services = Article.objects.filter(active=True,catagury__catagury="service")
    advantages = Article.objects.filter(active=True,catagury__catagury="advantage")
    about = Article.objects.filter(active=True,catagury__catagury="about")
    types_if_project = Article.objects.filter(active=True,catagury__catagury="types of project")
    projects = Project.objects.filter(active=True)
    context = {}
    if cataguries is not None:
        context['cataguries']=  cataguries
    if sliders is not None:
        context['sliders']=  sliders
    if services is not None:
        context['services']=  services
    if advantages is not None:
        context['advantages']=  advantages
    if about is not None:
        context['about']=  about
    if types_if_project is not None:
        context['types_of_projects'] =  types_if_project
    if projects is not None:
        context['projects'] =  projects

    return render(request,'theme/index.html',context)


def uhome(request):
    return render(request,'uheme/index.html')