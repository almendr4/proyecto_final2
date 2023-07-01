from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Bienvenidx a este sitio web! :)")
