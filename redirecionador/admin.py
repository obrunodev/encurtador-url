from django.contrib import admin

from redirecionador.models import LinkRedirecionamento


@admin.register(LinkRedirecionamento)
class LinkRedirecionamentoAdmin(admin.ModelAdmin):
    """
    Classe que representa o modelo de dados LinkRedirecionamento no admin.
    """
    list_display = ('title', 'url_curta', 'url_destino', 'clicks', 'created_at', 'updated_at')
    search_fields = ('title', 'url_curta', 'url_destino')
    list_filter = ('created_at', 'updated_at')
