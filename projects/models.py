from django.db import models
from django.utils.translation import gettext_lazy as _

PROJECTS_IMAGE_UPLOAD_TO = 'projects/'
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
  image = models.ImageField(upload_to=PROJECTS_IMAGE_UPLOAD_TO, blank=True)
  code_url = models.CharField(_("Código del proyecto"), max_length=100, default='', blank=True)
  demo_url = models.CharField(_("URL del proyecto"), max_length=100, default='', blank=True)
  type_project = models.CharField(
    _("Tipo del proyecto"),
    max_length=10,
    choices=Type.choices,
    default=Type.WORK,
  )
  platform = models.CharField(_("Plataforma"), max_length=10, default='', blank=True)
  role = models.CharField(_("Rol"), max_length=50, default='', blank=True)
  team = models.CharField(_("Equipo"), max_length=50, default='', blank=True)
  status = models.CharField(_("Estado"), max_length=50, default='', blank=True)
  