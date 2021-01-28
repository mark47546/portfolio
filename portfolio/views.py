from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForms

def index(request):
    if request.method == 'POST':
        forms = ContactForms(request.POST)
        if forms.is_valid():
            question = forms.save()
            question.save()
    else:
        forms = ContactForms()
    return render(request, 'portfolio/index.html', {'forms': forms})
