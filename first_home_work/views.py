from django.shortcuts import render

def fist_home_wokr(request):
    if request.method == 'GET':
        
        context ={ 
            'emodji' : "😈",
            'text':'Привет моя первая домашка',
            'run_string' : 'Hello World'
            }
        return render(request, template_name= 'index.html', context=context)
