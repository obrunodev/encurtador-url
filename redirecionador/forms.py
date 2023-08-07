from django import forms

from redirecionador.models import LinkRedirecionamento


class LinkRedirecionamentoForm(forms.ModelForm):
    """
    Classe que representa o formulário para o modelo de dados LinkRedirecionamento.
    """
    class Meta:
        model = LinkRedirecionamento
        fields = ['title', 'url_curta', 'url_destino']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url_curta': forms.TextInput(attrs={'class': 'form-control'}),
            'url_destino': forms.TextInput(attrs={'class': 'form-control'}),
        }
