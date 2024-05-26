if (Test-Path -Path ".venv") {
    Remove-Item -Recurse -Force ".venv"
}

py -m venv .venv

& .\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

python manage.py migrate
