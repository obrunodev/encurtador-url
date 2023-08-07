from django.db.models import F
from django.shortcuts import get_object_or_404, redirect, render

from redirecionador.forms import LinkRedirecionamentoForm
from redirecionador.models import LinkRedirecionamento


def index(request):
    """
    View para renderizar a página inicial do projeto.
    """
    links = LinkRedirecionamento.objects.all()
    context = {
        'form': LinkRedirecionamentoForm(),
        'links': links
    }
    
    if request.method == 'POST':
        form = LinkRedirecionamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('redirecionador:index')

    return render(request, 'redirecionador/index.html', context)


def redireciona_usuario(request, url_curta):
    """
    View para redirecionar o usuário para a URL de destino.
    """
    link = get_object_or_404(LinkRedirecionamento, url_curta=url_curta)
    if request.method == 'GET':
        link.clicks += 1
        link.save()
        # link.clicks = F('clicks') + 1
        # link.save(update_fields=['clicks'])
        return redirect(link.url_destino)
