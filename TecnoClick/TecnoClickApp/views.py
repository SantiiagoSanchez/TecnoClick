from django.shortcuts import render, HttpResponse
# Create your views here.

def home (request):

    return render(request, "TecnoClickApp/home.html")


def tienda (request):

    return render(request, "TecnoClickApp/store.html")



