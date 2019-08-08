from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from django.urls import reverse
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Card, Tag
from .utils import *

from .forms import *

def cards_list(request):
    search_lib = request.GET.get('search_g', '')

    if search_lib:
        cards = Card.objects.filter(Q(title__icontains=search_lib) | Q(body__icontains=search_lib) )
    else:
        cards = Card.objects.all()
    return render(request, 'card/index.html', context={'cards': cards})




class CardRead(ObjectReadMixin, View):
    model = Card
    template = 'card/card_read.html'

class CardCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = CardForm
    template = 'card/card_create.html'

class CardUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Card
    model_form = CardForm
    template = 'card/card_update.html'

class CardDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Card
    template = 'card/card_delete.html'
    redirect_url = 'cards_list_url'

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'card/tags_list.html', context={'tags': tags})


class TagRead(ObjectReadMixin, View):
    model = Tag
    template = 'card/tag_read.html'

class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = TagForm
    template = 'card/tag_create.html'

class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'card/tag_update.html'

class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'card/tag_delete.html'
    redirect_url = 'tags_list_url'
