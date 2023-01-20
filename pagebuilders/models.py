from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	deleted_at = models.DateTimeField(null=True, blank=True)

	class Meta:
		abstract = True


class Page(BaseModel):
	title = models.CharField(max_length=100)
	slug = models.SlugField(_("Slug"), max_length=255)


	class Meta:
		verbose_name = _("page")
		verbose_name_plural = _("pages")


class Section(BaseModel):
	name = models.CharField()
	slug = models.SlugField()
