from django.shortcuts import render

def index2(request):

    return render(
        request,
        'notes/index.html',
    )