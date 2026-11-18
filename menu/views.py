from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ProductoForm
from .models import Producto


class ProductoListView(ListView):
    model = Producto
    template_name = 'menu/producto_list.html'
    context_object_name = 'productos'

    def get_queryset(self):
        # Un solo JOIN en vez de N+1 consultas
        return Producto.objects.select_related('categoria')


class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'menu/producto_detail.html'
    context_object_name = 'producto'

    def get_queryset(self):
        return Producto.objects.select_related('categoria')


# LoginRequiredMixin siempre a la izquierda (regla MRO)
class ProductoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'menu/producto_form.html'
    success_url = reverse_lazy('producto_list')
    success_message = 'Producto "%(nombre)s" creado correctamente.'


class ProductoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'menu/producto_form.html'
    success_url = reverse_lazy('producto_list')
    success_message = 'Producto "%(nombre)s" actualizado correctamente.'


class ProductoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Producto
    template_name = 'menu/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')
    success_message = 'Producto eliminado correctamente.'
