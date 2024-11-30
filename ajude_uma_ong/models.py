from django.db import models

class ONG(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    email = models.EmailField()
    telefone = models.CharField(max_length=15, blank=True, null=True)
    site = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Pauta(models.Model):
    ong = models.ForeignKey(ONG, on_delete=models.CASCADE, related_name='pautas')
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    criada_em = models.DateTimeField(auto_now_add=True)
    prazo = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.ong.nome}"


class Ajuda(models.Model):
    pauta = models.ForeignKey(Pauta, on_delete=models.CASCADE, related_name='ajudas')
    nome_pessoa = models.CharField(max_length=255)
    email_pessoa = models.EmailField()
    mensagem = models.TextField()

    def __str__(self):
        return f"Ajuda de {self.nome_pessoa} para {self.pauta.titulo}"

