from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import generic
from .models import GdsModel
from django.core.paginator import Paginator
# Create your views here.
class ListView(generic.ListView):
    template_name='post/index.html'
    context_object_name='PostsList'
    paginate_by = 4
    def get_queryset(self):
        return GdsModel.objects.order_by('-date')

class DetailView(generic.DetailView):
    model = GdsModel
    template_name='post/detail.html'
    context_object_name='post'
