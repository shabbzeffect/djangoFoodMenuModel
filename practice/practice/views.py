from django.http import HttpResponse 

def hello(request):
    return HttpResponse("Hello from Django.....!!!!")

def about(request):
    return HttpResponse("This is about page")