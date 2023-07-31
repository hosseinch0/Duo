from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
# Create your views here.


def single_view(request):
    return render(request, "blog/single.html")
