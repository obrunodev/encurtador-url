from django.db import models


class LinkRedirecionamento(models.Model):
    """
    Classe que representa o modelo de dados para o redirecionamento.
    """
    title = models.CharField(max_length=100)
    url_curta = models.CharField(max_length=10, unique=True)
    url_destino = models.URLField()
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Link de Redirecionamento'
        verbose_name_plural = 'Links de Redirecionamento'
        ordering = ['title']

    def __str__(self):
        return self.title
