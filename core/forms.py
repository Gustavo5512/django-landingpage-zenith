from django import forms
from .models import Projeto, Lead

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = [
            'nome', 'slug', 'descricao_curta', 'thumbnail', 
            'youtube_url', 'tecnologias', 'performance_metrics', 
            'link_demo', 'link_repo', 'mostrar_live_view', 'mostrar_repo', 'categoria'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao_curta': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'youtube_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Ex: https://www.youtube.com/watch?v=dQw4w9WgXcQ'}),
            'tecnologias': forms.TextInput(attrs={'class': 'form-control'}),
            'performance_metrics': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'link_demo': forms.URLInput(attrs={'class': 'form-control'}),
            'link_repo': forms.URLInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['nome', 'email', 'whatsapp', 'descricao_projeto']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Seu nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Seu melhor e-mail'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': '(00) 00000-0000'}),
            'descricao_projeto': forms.Textarea(attrs={'class': 'form-control bg-dark text-white border-secondary', 'rows': 4, 'placeholder': 'Conte-nos sobre seu projeto...'}),
        }
