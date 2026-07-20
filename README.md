# 🔗 URL Shortener App

A minimal URL shortener built with **Python / Django**, deployed on **AWS EC2** via GitHub Actions CI/CD.

Paste a long URL → get a short code → track clicks.

## Architecture

```
User → Nginx (port 80) → Gunicorn (port 8000) → Django → SQLite
```

- **EC2 t3.micro** (Ubuntu 22.04, us-east-1)
- **Nginx** — reverse proxy + static files
- **Gunicorn** — WSGI server
- **SQLite** — local database (sufficient for single-instance Tier 1)
- **Elastic IP** — stable public address

## Features

| Feature | Details |
|---|---|
| Shorten URL | POST `/` with a long URL |
| Redirect | GET `/<code>` — 302 redirect + click counter |
| Stats | GET `/stats/<code>/` — clicks and metadata |
| Recent links | Home page shows the 10 most recent short URLs |
| Admin | `/admin/` — Django admin panel |

## Run Locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create a .env file
echo "SECRET_KEY=dev-secret-local" > .env
echo "DEBUG=True" >> .env

python manage.py migrate
python manage.py runserver
```

Open `http://localhost:8000`.

## Configuration

| Variable | Required | Description |
|---|---|---|
| `SECRET_KEY` | Yes | Django secret key (set via `DJANGO_SECRET_KEY` CI secret) |
| `DEBUG` | No | `True` for local dev, `False` in production |
| `ALLOWED_HOSTS` | No | Comma-separated hostnames (defaults to `*`) |

## Deployment

Deployment is fully automated via GitHub Actions:

| Stage | Action |
|---|---|
| `lint` | flake8 on `shortener/` and `manage.py` |
| `test` | Django test suite |
| `provision` | Terraform: EC2 + EIP + Security Group |
| `configure` | Ansible: install packages, deploy app, configure Nginx + systemd |
| `verify` | HTTP health check against the public IP |

Push to `main` triggers the pipeline. The live URL is:

```
http://<ec2-public-ip>/
```

(The IP is shown in the `provision` stage output after first deploy.)

## Operations

**View logs:**
```bash
ssh -i deploy_key ubuntu@<ec2-ip> sudo journalctl -u url-shortener -f
sudo tail -f /var/log/url-shortener-access.log
```

**Restart app:**
```bash
ssh -i deploy_key ubuntu@<ec2-ip> sudo systemctl restart url-shortener
```

**Run migrations manually:**
```bash
ssh -i deploy_key ubuntu@<ec2-ip>
cd /opt/url-shortener-app
sudo -u www-data venv/bin/python manage.py migrate
```

**Destroy infrastructure:**
Use the platform's Destroy action (dispatches `.github/workflows/destroy.yml`).
