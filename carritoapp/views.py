from django.shortcuts import render, HttpResponse

# Create your views here.
def tienda(request):
    return HttpResponse("Hola")
    #return render(request, "tienda.html")