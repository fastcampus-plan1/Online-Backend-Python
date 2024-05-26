if exist .venv (
    rmdir /s /q .venv
)

if exist db.sqlite3 (
    del db.sqlite3
)

py -m venv .venv

call .venv\Scripts\activate.bat

pip install -r requirements.txt

python my_project\manage.py migrate
