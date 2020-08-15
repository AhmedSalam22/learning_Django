from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView , CreateView , DeleteView 
from django.views.generic import ListView
from django.views import View
from .models import Make , Auto
from django.urls import reverse_lazy
# Create your views here.
class MainView(LoginRequiredMixin , View):
    def get(self , request):
        mc = Make.objects.all().count()
        al = Auto.objects.all()

        ctx = {
            'make_count': mc, 'auto_list': al
        }
        return render(request , "autos/main.html" , ctx)

class MakeView(LoginRequiredMixin , ListView):
    model = Make
    template_name = "autos/make_list.html"
    context_object_name = "make_list"

class MakeCreate(LoginRequiredMixin , CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:make_list')

class MakeUpdate(LoginRequiredMixin , UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:make_list')

class MakeDelete(LoginRequiredMixin , DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:make_list')

class AutoCreate(LoginRequiredMixin,CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

