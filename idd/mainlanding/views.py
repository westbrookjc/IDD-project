from django.shortcuts import render

def index(request):
        return render(request, 'mainlanding/home.html')

def about(request):
        return render(request, 'mainlanding/basic.html')

