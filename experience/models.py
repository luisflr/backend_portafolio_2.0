from django.db import models
from django.utils.translation import gettext_lazy as _

class Experience(models.Model):
  company = models.CharField(_("Empresa"), max_length=80)
  role = models.CharField(_("Rol"), max_length=50)
  initial_date = models.DateTimeField(_("Inicio"), max_length=80)
  end_date = models.DateTimeField(_("Fin"), max_length=80)
  description = models.CharField(_("Descripcion"), max_length=250)
  achievements = models.JSONField(
      _("Logros"),
      default=list, 
      blank=True,
      help_text="Logros"
  )
  stack = models.JSONField(
      _("Stack Tecnológico"),
      default=list, 
      blank=True,
      help_text="Stack Tecnológico"
  )
  order = models.IntegerField(_("Orden"), default=0)
