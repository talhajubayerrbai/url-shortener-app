from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(max_length=2000)),
                ('code', models.CharField(db_index=True, max_length=20, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('click_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
