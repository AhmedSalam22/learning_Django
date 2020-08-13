from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def session_cookies(request):
    resp.set_cookie('dj4e_cookie', '64d52e08', max_age=1000)
    num_vist = request.session.get("num_vist" , 0) + 1 
    request.session["num_vist"] = num_vist
    if num_vist > 4: del(request.session["num_vist"])
    return HttpResponse('view count='+str(num_vist))

