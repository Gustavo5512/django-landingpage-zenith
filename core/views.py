from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, TemplateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Projeto, Categoria, Lead, Certificado
from .forms import ProjetoForm, LeadForm

class PortfolioListView(ListView):
    model = Projeto
    template_name = 'core/portfolio.html'
    context_object_name = 'projetos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['certificados'] = Certificado.objects.all()
        return context

class ProjetoDeleteView(LoginRequiredMixin, DeleteView):
    model = Projeto
    success_url = reverse_lazy('core:portfolio')

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

class CertificadoCreateView(LoginRequiredMixin, CreateView):
    model = Certificado
    fields = ['nome', 'instituicao', 'logotipo', 'imagem_certificado', 'descricao', 'ordem']
    template_name = 'core/postar_certificado.html'
    success_url = reverse_lazy('core:portfolio')

class CertificadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Certificado
    success_url = reverse_lazy('core:portfolio')

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

class ProjetoCreateView(LoginRequiredMixin, CreateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = 'core/postar_projeto.html'
    success_url = reverse_lazy('core:portfolio')

    def form_valid(self, form):
        # Aqui podemos adicionar lógica extra se necessário
        import json
        metrics = self.request.POST.get('performance_metrics')
        if metrics:
            try:
                form.instance.performance_metrics = json.loads(metrics)
            except json.JSONDecodeError:
                form.instance.performance_metrics = {"error": "Invalid JSON"}
        return super().form_valid(form)

class ConfiguradorView(CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'core/configurador.html'
    success_url = reverse_lazy('core:portfolio')

    def form_valid(self, form):
        self.object = form.save()
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success', 'redirect_url': str(self.success_url)})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
        return super().form_invalid(form)

class LeadListView(LoginRequiredMixin, ListView):
    model = Lead
    template_name = 'core/lead_list.html'
    context_object_name = 'leads'
    ordering = ['-data_criacao']

def calcular_escopo(request):
    return JsonResponse({'status': 'deprecated'})

def filtrar_projetos(request):
    categoria_slug = request.GET.get('categoria')
    if categoria_slug == 'todos':
        projetos = Projeto.objects.all()
    else:
        projetos = Projeto.objects.filter(categoria__slug=categoria_slug)
    
    # Renderizar apenas o snippet dos cards para o AJAX
    return render(request, 'core/includes/projeto_cards.html', {'projetos': projetos})
