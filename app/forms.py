from django.forms import ModelForm
from app.models import Query

class QueryForm(ModelForm):
	class Meta:
		model = Query
		fields = ['name','email','message']
