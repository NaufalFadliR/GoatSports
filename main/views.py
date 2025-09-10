from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406350785',
        'name': 'Naufal Fadli Rabbani',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
