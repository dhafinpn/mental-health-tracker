from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306221112',
        'name': 'Dhafin Putra Nugraha',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
# Create your views here.
