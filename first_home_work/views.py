from django.shortcuts import render
from django.views import generic


class FirstPageView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'emoji': '🎬',
            'text': 'Здесь собраны лучшие фильмы.',
            'run_string': 'Каждый найдет своё.Приятного просмотра'
        })
        return context

# def first_page_view(request):
#     if request.method == 'GET':
        
#         context = {
#             'emoji': '🎬',
#             'text': 'Здесь собраны лучшие фильмы.',
#             'run_string': 'Каждый найдет своё.Приятного просмотра'
#         }
#     return render(request, template_name='index.html', context=context)