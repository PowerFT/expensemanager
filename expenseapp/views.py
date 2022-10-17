from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
# Create your views here.
def render_home(request):
    return render(request,"expense_home.html")