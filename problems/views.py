from django.http import HttpResponse


def index(request):
    return HttpResponse("Thers is nothing now.")
