from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Motorista, Veiculo, Controle
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    return render(request, "app_controle/home.html")

class MotoristaListView(ListView):
    model = Motorista

class VeiculoListView(ListView):
    model = Veiculo

class MotoristaCreateView(CreateView):
    model = Motorista
    fields = "__all__"
    success_url = reverse_lazy("motorista_list")

class VeiculoCreateView(CreateView):
    model = Veiculo
    fields = ['placa', 'marca', 'veiculo', 'km_troca_oleo']
    success_url = reverse_lazy("veiculo_list")

class MotoristaUpdateView(UpdateView):
    model = Motorista
    fields = ['nome', 'telefone']
    success_url = reverse_lazy("motorista_list")

class VeiculoUpdateView(UpdateView):
    model = Veiculo
    fields = ['placa', 'marca', 'veiculo', 'km_troca_oleo']
    success_url = reverse_lazy('veiculo_list')

class MotoristaDeleteView(DeleteView):
    model = Motorista
    success_url = reverse_lazy("motorista_list")

class VeiculoDeleteView(DeleteView):
    model = Veiculo
    success_url = reverse_lazy("veiculo_list")

class ControleListView(ListView):
    model = Controle
    template_name = 'controle_list.html'
    context_object_name = 'controles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['motoristas'] = Motorista.objects.all()
        context['veiculos'] = Veiculo.objects.all()

        motoristas_existem = context['motoristas'].exists()
        veiculos_existem = context['veiculos'].exists()
        controles_existem = Controle.objects.exists()
 
        if not motoristas_existem and not veiculos_existem:
            context['mensagem'] = 'Não existem registros de motoristas e veículos.'
        elif not motoristas_existem:
            context['mensagem'] = 'Não existem registros de motoristas.'
        elif not veiculos_existem:
            context['mensagem'] = 'Não existem registros de veículos.'
        elif not controles_existem and (veiculos_existem and motoristas_existem):
            context['mensagem'] = 'Não existem registros de controle'
        else:
            context['mensagem'] = 'Existem registros de motoristas e veículos.'
        
        for veiculo in Veiculo.objects.all():
            if not Controle.objects.filter(veiculo=veiculo).exists():
                veiculo.disponivel = True
                veiculo.save()
                
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        data_saida = self.request.GET.get('data_saida')
        
        if data_saida:
            queryset = queryset.filter(data_saida=data_saida)
        return queryset

class ControleCreateView(CreateView):
    model = Controle
    fields = ['veiculo', 'motorista', 'data_saida', 'hora_saida', 'km_saida', 'destino', 'data_retorno', 'hora_retorno', 'km_retorno']
    success_url = reverse_lazy("controle_list")

    def form_valid(self, form):
        veiculo = form.cleaned_data['veiculo']
        veiculo.disponivel = False
        veiculo.save()
        return super().form_valid(form)

class ControleUpdateView(UpdateView):
    model = Controle
    fields = ['veiculo', 'motorista', 'data_saida', 'hora_saida', 'km_saida', 'destino', 'data_retorno', 'hora_retorno', 'km_retorno']
    success_url = reverse_lazy('controle_list')

class ControleDeleteView(DeleteView):
    model = Controle
    context_object_name = 'controle'
    success_url = reverse_lazy("controle_list")

class ControleDetailView(DetailView):
    model = Controle
    context_object_name = 'controle_view'
    success_url = reverse_lazy("controle_list")

def pagina_nao_encontrada(request, exception):
    return render(request, '404.html', status=404)
