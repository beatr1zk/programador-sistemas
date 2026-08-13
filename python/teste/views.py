from django.http import HttpResponse

def recebe(request):
    idade = int(request.GET["idade"])

    if idade < 18:
        return HttpResponse("Menor de idade")
    else:
        return HttpResponse("Maior de idade")