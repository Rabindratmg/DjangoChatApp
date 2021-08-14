from django.shortcuts import render
from . thread import ThreadExample

# Create your views here.


def Home(request):
    ThreadExample().start()
    context={
            "hi":"hello",
    }
    
    return render(request,"index.html",context)
