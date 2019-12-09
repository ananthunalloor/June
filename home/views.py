from django.shortcuts import render

# Create your views here.
def Home(request):
    template = 'index.html'
    context = {}
    return render(request,template,context)
