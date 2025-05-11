from django.shortcuts import render
from django.http import HttpResponse


def fist_home_wokr(request):
    if request.method == 'GET':
        context = {
            'emoji': ":)",
            'text' : 'First project',
            'run_string': 'lalalalalalallaallalalal'
        }
        return render(request, template_name='index.html', context=con)