from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def comingout(request):
    return render(request, 'comingout.html')
def community(request):
    return render(request, 'community.html')

def culture(request):
    return render(request, 'culture.html')

def gettoknow(request):
    return render(request, 'gettoknow.html')