from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Projects(models.Model):
  class Type(models.TextChoices):
    WORK = 'Trabajo'
    PERSONAL = 'Personal'

  name = models.CharField(_("Nombre del proyecto"), max_length=100)
  description = models.CharField(_("Descripción"), max_length=250)
  stack = models.JSONField(
      _("Stack Tecnológico"),
      default=list, 
      blank=True,
      help_text="Stack Tecnológico"
  )
  order = models.IntegerField(_("Orden"), default=0)
  type_project = models.CharField(
    _("Tipo del proyecto"),
    max_length=10,
    choices=Type.choices,
    default=Type.WORK,
  )
  