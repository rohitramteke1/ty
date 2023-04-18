from django.shortcuts import render, HttpResponse

# Create your views here.

def loginapp(request):
    return render(request, 'index.html')