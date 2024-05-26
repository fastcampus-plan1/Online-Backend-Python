# ���� ȯ�� ����
if (Test-Path -Path ".venv") {
    Remove-Item -Recurse -Force ".venv"
}

# �����ͺ��̽� ���� ����
if (Test-Path -Path "db.sqlite3") {
    Remove-Item -Force "db.sqlite3"
}

# ���� ȯ�� ����
py -m venv .venv

# ���� ȯ�� Ȱ��ȭ
& .\.venv\Scripts\Activate.ps1

# �ʿ��� ��Ű�� ��ġ
pip install -r requirements.txt

# �����ͺ��̽� ���̱׷��̼�
python manage.py migrate

# ȯ�� ���� ����
$env:DJANGO_SUPERUSER_USERNAME="admin"
$env:DJANGO_SUPERUSER_EMAIL="admin@example.com"
$env:DJANGO_SUPERUSER_PASSWORD="password"

# �������� ����
python manage.py createsuperuser --noinput
