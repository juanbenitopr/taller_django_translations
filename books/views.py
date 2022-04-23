from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import gettext as _

from django.views import View

from books.models import Book


class ListBookView(View):
    def get(self, request):
        messages.info(request, _('Mostrando el listado de libros'))
        return render(request, 'list_book.html',
                      context={'books': Book.objects.all()})
