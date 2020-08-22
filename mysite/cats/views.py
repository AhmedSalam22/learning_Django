from django.shortcuts import render
from django.views.generic import DeleteView , ListView , UpdateView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Cat, Breed
# Create your views here.

class CatList(LoginRequiredMixin , ListView):
    model = Cat

class CatCreate(LoginRequiredMixin , CreateView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:all")

class CatUpdate(LoginRequiredMixin , UpdateView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:all")

class CatDelete(LoginRequiredMixin , DeleteView):
    model = Cat
    success_url = reverse_lazy("cats:all")



class BreedView(LoginRequiredMixin , ListView):
    model = Breed

class BreedCreate(LoginRequiredMixin , CreateView):
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy("cats:all")

class BreedUpdate(LoginRequiredMixin , UpdateView):
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy("cats:all")

class BreedDelete(LoginRequiredMixin , DeleteView):
    model = Breed
    success_url = reverse_lazy("cats:all")