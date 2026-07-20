import random
import string
from django.db import models
from django.utils import timezone


def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(chars, k=length))
        if not ShortURL.objects.filter(code=code).exists():
            return code


class ShortURL(models.Model):
    original_url = models.URLField(max_length=2000)
    code = models.CharField(max_length=20, unique=True, db_index=True)
    created_at = models.DateTimeField(default=timezone.now)
    click_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.code} -> {self.original_url}"

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_code()
        super().save(*args, **kwargs)
