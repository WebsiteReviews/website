from django import forms

class ReviewForm(forms.Form):
    review_text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Напишите вашу рецензию', 'class': 'text_of_rewiews col-11'}))