if exist .venv (
    rmdir /s /q .venv
)

py -m venv .venv

call .venv\Scripts\activate.bat

pip install -r requirements.txt

python manage.py migrate
