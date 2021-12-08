from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request=request, template_name='home.html', context={})
    
def genre():
    pass

def edit():
    pass

def post():
    pass