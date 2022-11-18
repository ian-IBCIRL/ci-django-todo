from django.shortcuts import render, HttpResponse


# Create your views here.
def say_hi2(request):
    return HttpResponse("hello world 2 !")


def say_hitop(request):
    return HttpResponse("hello world from the top !")


def say_hi(request):
    return HttpResponse("hello world !")



