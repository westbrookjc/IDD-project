from django.shortcuts import render

def index(request):
        return render(request, 'mainlanding/home.html')

def about(request):
        return render(request, 'mainlanding/basic.html', {'content':['Hello! I\'m an engineering graduate with a passion for data. If you would like to contact me, please email me at:','westbrookjamesc@gmail.com']})

