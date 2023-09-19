from django.forms import ModelForm
from main.models import Item

class ProdutForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]