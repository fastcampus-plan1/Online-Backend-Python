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
python my_project\manage.py migrate
