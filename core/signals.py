from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Lead

@receiver(post_save, sender=Lead)
def notify_new_lead(sender, instance, created, **kwargs):
    if created:
        # Email para o time Zenith
        send_mail(
            'Novo Lead Recebido - Zenith Portfolio',
            f'Novo lead recebido: {instance.nome} ({instance.email}). Complexidade: {instance.estimativa_complexidade}',
            'no-reply@zenith.com',
            ['team@zenith.com'],
            fail_silently=True,
        )
        
        # Email de confirmação para o cliente
        send_mail(
            'Recebemos seu pedido! - Zenith',
            f'Olá {instance.nome}, obrigado pelo interesse! Nossa equipe analisará seu pedido de complexidade {instance.estimativa_complexidade} e entrará em contato em breve.',
            'no-reply@zenith.com',
            [instance.email],
            fail_silently=True,
        )
