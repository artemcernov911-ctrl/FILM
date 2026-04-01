from .models import Films
from django.forms import ModelForm

class News_Films(ModelForm):
	class Meta:
		model = Films
		fields = ['name', 'description', 'review']