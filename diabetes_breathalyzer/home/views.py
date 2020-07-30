from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render , reverse , redirect 


# Create your views here.
def index(request):
	return render(request,'home/index.html')