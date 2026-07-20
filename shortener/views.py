from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import ShortURL
from .forms import ShortenForm


def index(request: HttpRequest) -> HttpResponse:
    """Home page: shorten a URL and display the result."""
    short_url = None
    form = ShortenForm()

    if request.method == 'POST':
        form = ShortenForm(request.POST)
        if form.is_valid():
            original = form.cleaned_data['url']
            obj, _ = ShortURL.objects.get_or_create(original_url=original)
            short_url = request.build_absolute_uri(f'/{obj.code}')

    recent = ShortURL.objects.order_by('-created_at')[:10]
    return render(request, 'shortener/index.html', {
        'form': form,
        'short_url': short_url,
        'recent': recent,
    })


def redirect_short(request: HttpRequest, code: str) -> HttpResponse:
    """Redirect a short code to its original URL and increment click count."""
    obj = get_object_or_404(ShortURL, code=code)
    obj.click_count += 1
    obj.save(update_fields=['click_count'])
    return redirect(obj.original_url, permanent=False)


def stats(request: HttpRequest, code: str) -> HttpResponse:
    """Show stats for a short URL."""
    obj = get_object_or_404(ShortURL, code=code)
    short_url = request.build_absolute_uri(f'/{obj.code}')
    return render(request, 'shortener/stats.html', {'obj': obj, 'short_url': short_url})
