from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from employers.models import Employé


@receiver(post_save, sender=User)
def post_save_create_employe(sender, instance, created, **kwargs):
    print('sender:', sender)
    print('instance:', instance)
    print('created:', created)
    if created:
        Employé.objects.create(user=instance)