from django.shortcuts import render
from . thread import ThreadExample

# Create your views here.


def Home(request):
    ThreadExample().start()
    context={
            "hi":"Hello",
    }
    
    return render(request,"index.html",context)
