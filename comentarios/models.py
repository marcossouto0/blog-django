from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Comentario(models.Model):
  nome_comentario = models.CharField(max_length=150, verbose_name='Nome')
  email_comentario = models.EmailField(verbose_name='E-Mail')
  comentario = models.TextField(verbose_name='Comentario')
  post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE)
  usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank = True, null = False)
  data_comentario = models.DateTimeField(default=timezone.now)
  publicado_comentario = models.BooleanField(default=False)
  
  def __str__(self):
    return self.nome_comentario