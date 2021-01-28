from django.shortcuts import render
from portfolio.models import Porfolio

def index(request):
    portfolios = Porfolio.objects.all()
    context = {
        'portfolios':portfolios
    }
    return render(request,'index.html',context)

def detail(request,pk):
    portfolio = Porfolio.objects.get(pk=pk)
    context = {
        'portfolio':portfolio
    }
    return render(request,'deatil.html',context)