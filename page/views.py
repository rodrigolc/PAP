from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def view_template(request,path):
	print(path)
	return render(request,path)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")