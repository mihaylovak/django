from django import forms

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product