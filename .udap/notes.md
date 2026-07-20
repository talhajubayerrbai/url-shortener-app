# url-shortener-app — Build Notes

## Project
- Cloud: AWS us-east-1, EC2 t3.micro (Ubuntu 22.04)
- Stack: Python 3.11 / Django 4.2 / SQLite / Gunicorn / Nginx / Whitenoise
- VCS: GitHub
- Tier 1 (single instance, no managed DB)

## Status
- [x] Architecture written (.udap/architecture.d2)
- [x] Pipeline written (.udap/pipeline.yaml)
- [x] Django app: shortener/ (models, views, forms, urls, admin, tests, migrations)
- [x] Templates: base.html, index.html, stats.html
- [x] Ansible playbook: ansible/site.yml (installs nginx, gunicorn, systemd unit)
- [x] Terraform IaC: infra/ (EC2, SG, EIP, key pair — default VPC)
- [x] requirements.txt: django, gunicorn, whitenoise, python-dotenv
- [ ] DJANGO_SECRET_KEY secret to set before deploy
- [ ] validate_project
- [ ] create_repo_and_push
- [ ] deploy

## Key Decisions
- SQLite on-disk (Tier 1 — no RDS). db.sqlite3 lives in app_dir, owned by www-data.
- Gunicorn binds 127.0.0.1:8000; nginx proxies on port 80.
- App deployed to /opt/url-shortener-app via ansible.builtin.copy.
- venv at /opt/url-shortener-app/venv; systemd ExecStart uses absolute venv path.
- EIP provides a stable IP; output ec2_public_ip threaded to configure+verify via job outputs.
- ec2_public_ip is NOT secret-derived — safe to pass via job outputs.
- DJANGO_SECRET_KEY injected via ansible env var → env.j2 template → .env file.

## Gotchas / Pitfalls
- PROJECT_NAME is a repo secret — never export derived hostnames via job outputs.
- verify stage uses curl --retry 10 --retry-delay 15 for boot time.
- backend "s3" {} is empty — backend-config flags come from platform at runtime.
- TF_VAR_secret_key declared in variables.tf (unused by TF itself) to avoid TF prompting.
