from django import forms
from .models import Checkout, ImageModel


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['name', 'email', 'phone', 'payment_method']
        widgets = {
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
        }



class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image','title','price']