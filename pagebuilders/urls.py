from django.urls import path
from pagebuilders import views

app_name = "pagebuilders"

urlpatterns = [
	path("", views.PageListView.as_view())
]
