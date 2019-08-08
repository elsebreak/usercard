from django.http import HttpResponse
from django.shortcuts import redirect


def redirect_card(request):
    return redirect('cards_list_url', permanent=True)
