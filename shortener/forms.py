from django import forms


class ShortenForm(forms.Form):
    url = forms.URLField(
        label='Long URL',
        max_length=2000,
        widget=forms.URLInput(attrs={
            'class': 'form-input',
            'placeholder': 'https://example.com/very/long/url',
        })
    )
