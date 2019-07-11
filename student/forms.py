from django import forms
from .models import ShopInfo

class Listform(forms.ModelForm):
	class Meta:
		model = ShopInfo
		fields = ['ShopName','Rent','PaidRent','comments']