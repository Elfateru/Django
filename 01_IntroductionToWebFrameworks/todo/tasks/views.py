from django.http import HttpResponse

from django.views import View
from random import shuffle

# class ToDoView(View):
#
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('<ul>'
#                             '<li>Установить python</li>'
#                             '<li>Установить django</li>'
#                             '<li>Запустить сервер</li>'
#                             '<li>Порадоваться результату</li>'
#                             '</ul>')
class ToDoView(View):

    def get(self, request, *args, **kwargs):
        response_list = ['<li>Установить python</li>',
                         '<li>Установить django</li>',
                         '<li>Запустить сервер</li>',
                         '<li>Порадоваться результату</li>']
        shuffle(response_list)
        return HttpResponse('<ul>' + ''.join(response_list) + '</ul>')




