from django.db import models
from django.utils.text import slugify

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome

    @property
    def tecnologias_list(self):
        return [t.strip() for t in self.tecnologias.split(',') if t.strip()]

    class Meta:
        verbose_name_plural = "Categorias"

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    descricao_curta = models.TextField()
    thumbnail = models.ImageField(upload_to='portfolio/thumbnails/')
    youtube_url = models.URLField(blank=True, null=True, help_text="Link do vídeo no YouTube")
    tecnologias = models.CharField(max_length=200) # Ex: React, Django, AWS
    performance_metrics = models.JSONField(default=dict) # Score do Lighthouse, etc.
    link_demo = models.URLField(blank=True)
    link_repo = models.URLField(blank=True)
    mostrar_live_view = models.BooleanField(default=True)
    mostrar_repo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='projetos')
    data_criacao = models.DateTimeField(auto_now_add=True)

    @property
    def youtube_id(self):
        if not self.youtube_url:
            return None
        # Suporta vários formatos de link do YouTube (v=, /v/, embed/, youtu.be/, watch?v=, shorts/)
        import re
        regex = r'(?:v=|\/v\/|embed\/|youtu\.be\/|watch\?v=|\/shorts\/|\/)([a-zA-Z0-9_-]{11})'
        match = re.search(regex, self.youtube_url)
        return match.group(1) if match else None

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Lead(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    descricao_projeto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.whatsapp}"

class Certificado(models.Model):
    nome = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    instituicao = models.CharField(max_length=200)
    logotipo = models.ImageField(upload_to='certificados/logos/')
    imagem_certificado = models.ImageField(upload_to='certificados/arquivos/')
    descricao = models.TextField()
    ordem = models.IntegerField(default=0)
    data_conclusao = models.DateField(null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordem', '-data_criacao']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
