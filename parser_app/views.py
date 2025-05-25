from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from . import models, froms

class RezkaListView(generic.ListView):
    template_name = 'parser_films/parser_film_list.html'
    context_object_name = 'rezka'
    model= models.Parser_Rezka

    def get_queryset(self):
        return self.model.objects.all()
    
class ParserForm(generic.FormView):
    template_name = 'parser_library/parser_form.html'
    form_class = forms.ParserForm

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<h1>парсинг успешно завершен !!</h1>')
        
        else:
            return super(ParserForm, self).post(request,*args, **kwargs)


    
