from django.shortcuts import render

from random import randint

def home(request):
    data = [
        "Believe you can and you're halfway there.",
        "The journey of a thousand miles begins with one step.",
        "It is never too late to be what you might have been.",
        "If you cannot do great things, do small things in a great way.",
        "Talent wins games, but teamwork and intelligence wins championships.",
    ]
    n=len(data)
    n-=1
    i=randint(0,n)
    context = {
        "data":data[i]
    }

    return render(request,"page1/home.html",context)
