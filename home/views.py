from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    university = 'Karabuk University'
    dept = 'Computer Engineering'
    context = {'university': university, 'department':dept}
    return render(request, 'index.html', context)
