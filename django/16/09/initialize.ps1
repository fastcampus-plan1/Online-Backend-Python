if (Test-Path -Path ".venv") {
    Remove-Item -Recurse -Force ".venv"
}

if (Test-Path -Path "db.sqlite3") {
    Remove-Item -Force "db.sqlite3"
}

py -m venv .venv

& .\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

python manage.py migrate

$env:DJANGO_SUPERUSER_USERNAME="admin"
$env:DJANGO_SUPERUSER_EMAIL="admin@example.com"
$env:DJANGO_SUPERUSER_PASSWORD="password"
python manage.py createsuperuser --noinput
