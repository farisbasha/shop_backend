from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import Product, ProductTag

@receiver(post_save, sender=Product)
def add_new_tag(sender, instance, created, **kwargs):
    if created:
        ProductTag.objects.create(product=instance, tag='NEW')
