from django.http import HttpResponse
from django.shortcuts import render 
from django.template import loader


def test(request):
    temp = loader.get_template('index.html')
    return HttpResponse(temp.render())
    # return render(request, 'index.html')