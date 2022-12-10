from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': "Главная страница"
    }
    return render(request, "home/home.html", context=context)
