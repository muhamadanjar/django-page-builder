from django.views.generic.base import ContextMixin

class ContextTitleMixin(ContextMixin):
	title_page = ''
	subtitle_page = ''

	def get_title_page(self):
		return self.title_page

	def get_subtitle_page(self):
		return self.subtitle_page