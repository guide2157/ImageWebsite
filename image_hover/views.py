from django.shortcuts import render

# Create your views here.


def hover_image(request):
    return render(request, "images.html")


def welcome(request):
    return render(request, "index.html")
