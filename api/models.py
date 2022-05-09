from django.utils.translation import gettext_lazy as _
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Worker(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    phone_number = PhoneNumberField()

    def __str__(self) -> str:
        return str(self.name)


class SellsPoint(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    worker = models.ForeignKey(Worker, verbose_name=_("worker"), on_delete=models.CASCADE, related_name="sell_points")

    def __str__(self) -> str:
        return str(self.name)
    
    def get_worker_phone_number(self):
        return self.worker.phone_number


class Visit(models.Model):
    time = models.DateTimeField(_("Time visited"), auto_now=False, auto_now_add=True)
    sells_point = models.ForeignKey(SellsPoint, verbose_name=_("sells_point"), on_delete=models.CASCADE, related_name="visits")
    latitude = models.FloatField(_("Latitude"))
    longitude = models.FloatField(_("Longitude"))

    def __str__(self) -> str:
        return str(self.time)