from django.shortcuts import render_to_response
from django.http import HttpResponse


# Create your views here.
def myfirstview(requset):
    return HttpResponse('hello')


def hello(request, num):
    if isinstance(num, int):
        return HttpResponse('hello $d', num)
    else:
        return HttpResponse('hello string {s}'.format(s=num))


def html(request):
    return render_to_response('1.html',{'name':'hello'})
